from datetime import datetime

from rich.table import Table

from netwatch.models import HostConfig
from netwatch.ping import ping_host
from netwatch.ports import check_tcp_port


def format_ports(host: str, ports: list[int]) -> str:
    """Check configured TCP ports and return formatted results"""
    
    if not ports:
        return "-"
    
    results = []
    
    for port in ports:
        result = check_tcp_port(host, port)
        
        if result.open:
            results.append(f"[green]{port} ✅ [/green]")
            
        else:
            results.append(f"[red]{port} ❌ [/red]")
    
    return ", ".join(results)

def build_status_table(hosts: list[HostConfig]) -> Table:
    """Check all configured hosts and return a Rich Status table."""
    
    table = Table(title="Host Status")
    
    table.add_column("Name")
    table.add_column("Host")
    table.add_column("Status")
    table.add_column("Latency")
    table.add_column("TCP Ports")
    
    for host_config in hosts:
        result = ping_host(host_config.host)
        
        if result.reachable:
            status = "[green]ONLINE[/green]"
            
            latency = (
                f"{result.latency_ms:.2f} ms"
                if result.latency_ms is not None
                else "N/A"
                
            )
        else:
            status = "[red]OFFLINE[/red]"
            latency = "--"
            
        ports = format_ports(
            host_config.host,
            host_config.ports,
        )
        
        table.add_row(
            host_config.name,
            result.host,
            status,
            latency,
            ports,
        )
        
    return table
def get_timestamp() -> str:
    """Return the current local timestamp."""
    
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                     