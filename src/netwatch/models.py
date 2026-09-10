from dataclasses import dataclass, field


@dataclass
class HostConfig:
    """Configuration for a host monitored by NetWatch"""
    
    name: str
    host: str
    ports: list[int] = field(default_factory=list)
    
    