from pathlib import Path

from rich.console import Console
from rich.table import Table

from netwatch.config import load_hosts
from netwatch.ping import ping_host
from netwatch.ports import check_tcp_port

console = Console()

CONFIG_PATH = Path("config/hosts.json")

def format_ports(host: str, ports: list[int]) -> str:
    """Check configured TCP ports and format their status."""

    if not ports:
        return "—"

    results = []

    for port in ports:
        result = check_tcp_port(host, port)

        if result.open:
            results.append(f"[green]{port} ✓[/green]")
        else:
            results.append(f"[red]{port} ✗[/red]")

    return ", ".join(results)

def main() -> None:
    """Run the NetWatch application."""
    
    console.print() 
    console.print("[bold cyan]NetWatch Python[/bold cyan]")
    console.print("Network monitoring and diagnostics toolkit")
    console.print()
    
    try:
        hosts = load_hosts(CONFIG_PATH)
    except (FileNotFoundError, ValueError) as error:
        console.print(f"[red]Configuration error:[/red] {error}")
        return
    
        
    # Create ONE table before checking the hosts
    table = Table(title="Host Status")
    
    table.add_column("Name")
    table.add_column("Host")
    table.add_column("Status")
    table.add_column("Latency")
    table.add_column("TCP Ports")
    
    # Check each host and add ONE row to the existing table
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
    # Print the completed table AFTER the loop
    console.print(table)
        
if __name__ == "__main__":
    main()



    
