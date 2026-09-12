import json
from pathlib import Path

from netwatch.models import HostConfig, NetWatchConfig


def load_config(config_path: str | Path) -> NetWatchConfig:
    """Load host configuration from a json file"""
    
    path = Path(config_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
        
    if "hosts" not in data:
        raise ValueError("Configuration must contain 'hosts' section")
    
    refresh_interval = data.get("refresh_interval", 10)
    
    if not isinstance(refresh_interval, int) or refresh_interval < 1:
        raise ValueError("refresh_interval must be a possitive integer")
    
    hosts = []
    
    for item in data["hosts"]:
        if "name" not in item or "host" not in item:
            raise ValueError(
                "Each host must contain 'name' and 'host'."
                             
            )
            
        hosts.append(
            HostConfig(
                name=item["name"],
                host=item["host"],
                ports=item.get("ports", []),
            )
        )
        
    return NetWatchConfig(
        refresh_interval=refresh_interval,
        hosts=hosts,
    )
            
