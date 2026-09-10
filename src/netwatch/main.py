from pathlib import Path

from rich.console import Console
from rich.table import Table

from netwatch.config import load_hosts
from netwatch.ping import ping_host

console = Console()

CONFIG_PATH = Path("config/hosts.json")

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
            

            
        table.add_row(
            host_config.name,
            result.host,
            status,
            latency,
        )
    # Print the completed table AFTER the loop
    console.print(table)
        
if __name__ == "__main__":
    main()



    
