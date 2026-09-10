import subprocess
from unittest.mock import patch

import pytest

from netwatch.ping import _extract_latency, ping_host


@pytest.mark.parametrize(
    ("system", "flags"),
    [
        ("Darwin", ["-c", "1", "-W", "2000"]),
        ("Linux", ["-c", "1", "-W", "2"]),
        ("Windows", ["-n", "1", "-w", "2000"]),
    ],
)
def test_ping_timeout_units_and_latency(system, flags):
    response = subprocess.CompletedProcess(
        args=[], returncode=0,
        stdout="64 bytes from 1.1.1.1: icmp_seq=0 ttl=55 time=6.412 ms\n",
    )
    with patch("netwatch.ping.platform.system", return_value=system), patch(
        "netwatch.ping.subprocess.run", return_value=response
    ) as run:
        result = ping_host("1.1.1.1")

    run.assert_called_once_with(
        ["ping", *flags, "1.1.1.1"],
        capture_output=True, text=True, timeout=3, check=False,
    )
    assert result.reachable
    assert result.latency_ms == 6.412


def test_extract_latency():
    output = "64 bytes from 1.1.1.1: icmp_seq=0 ttl=57 time=7.42 ms"

    latency = _extract_latency(output)

    assert latency == 7.42


def test_extract_latency_less_than_one_ms():
    output = "64 bytes from 127.0.0.1: time<1 ms"

    latency = _extract_latency(output)

    assert latency == 1.0


def test_extract_latency_when_missing():
    output = "Request timeout for icmp_seq 0"

    latency = _extract_latency(output)

    assert latency is None

