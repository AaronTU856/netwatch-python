import json
from pathlib import Path

from netwatch.models import HostConfig


def load_hosts(config_path: str | Path) -> list[HostConfig]:
    """Load host configuration from a json file"""
    
    path = Path(config_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
        
    if "hosts" not in data:
        raise ValueError("Configuration must contain 'hosts' section")
    
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
        
    return hosts
            
