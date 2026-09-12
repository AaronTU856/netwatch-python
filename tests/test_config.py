import json

import pytest

from netwatch.config import load_config


def test_load_hosts_from_valid_config(tmp_path):
    config_file = tmp_path / "hosts.json"

    config_data = {
        "hosts": [
            {
                "name": "Test Server",
                "host": "127.0.0.1",
                "ports": [80, 443],
            }
        ]
    }

    config_file.write_text(
        json.dumps(config_data),
        encoding="utf-8",
    )

    config = load_config(config_file)

    assert len(config.hosts) == 1
    assert config.hosts[0].name == "Test Server"
    assert config.hosts[0].host == "127.0.0.1"
    assert config.hosts[0].ports == [80, 443]


def test_load_hosts_missing_file(tmp_path):
    missing_file = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        load_config(missing_file)


def test_load_hosts_missing_hosts_section(tmp_path):
    config_file = tmp_path / "hosts.json"

    config_file.write_text(
        json.dumps({"devices": []}),
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_config(config_file)


def test_load_hosts_missing_required_field(tmp_path):
    config_file = tmp_path / "hosts.json"

    config_data = {
        "hosts": [
            {
                "name": "Broken Host",
                "ports": [80],
            }
        ]
    }

    config_file.write_text(
        json.dumps(config_data),
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_config(config_file)