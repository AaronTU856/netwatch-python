import socket
from dataclasses import dataclass


@dataclass
class PortResult:
    host: str
    port: int
    open: bool
    
def check_tcp_port(
    host: str,
    port: int,
    timeout: float = 1.0,
) -> PortResult:
    """Check whether a TCP port is accepting connections"""

    try:
        with socket.create_connection(
            (host,port),
            timeout=timeout,
        ):
            return PortResult(
                host=host,
                port=port,
                open=True,
            )
            
    except (TimeoutError, ConnectionRefusedError, OSError):
            
        return PortResult(
            host=host,
            port=port,
            open=False,
        )