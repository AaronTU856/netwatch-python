import platform
import re
import subprocess
from dataclasses import dataclass


@dataclass
class PingResult:
    host: str
    reachable: bool
    latency_ms: float | None


def ping_host(host: str, timeout: int = 2) -> PingResult:
    """
    Ping a host once and return whether it is reachable
    together with the measured latency.
    """

    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", "-w", str(timeout * 1000), host]
    elif system == "darwin":
        # macOS expects -W in milliseconds; Linux expects seconds.
        command = ["ping", "-c", "1", "-W", str(timeout * 1000), host]
    else:
        command = ["ping", "-c", "1", "-W", str(timeout), host]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout + 1,
            check=False,
        )

        if result.returncode != 0:
            return PingResult(
                host=host,
                reachable=False,
                latency_ms=None,
            )

        latency = _extract_latency(result.stdout)

        return PingResult(
            host=host,
            reachable=True,
            latency_ms=latency,
        )

    except subprocess.TimeoutExpired:
        return PingResult(
            host=host,
            reachable=False,
            latency_ms=None,
        )


def _extract_latency(output: str) -> float | None:
    """
    Extract latency from standard ping output.
    """

    match = re.search(r"time[=<]([\d.]+)\s*ms", output)

    if match:
        return float(match.group(1))

    return None



