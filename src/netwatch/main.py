from rich.console import Console
from rich.table import Table

from netwatch.ping import ping_host

console = Console()


def main() -> None:
    """Run the NetWatch application."""
    
    hosts = [
        "1.1.1.1",
        "8.8.8.8",
        "127.0.0.1",
    
        
    ]
    
    
    console.print() 
    console.print("[bold]NetWatch Python[/bold]")
    console.print("Network monitoring and diagnostics toolkit")
    console.print()
    
    # Create ONE table before checking the hosts
    table = Table(title="Host Status")
    
    table.add_column("Host")
    table.add_column("Status")
    table.add_column("Latency")
    
    # Check each host and add ONE row to the existing table
    for host in hosts:
        result = ping_host(host)
        
        if result.reachable:
            status = "[green]ONLINE[/green]"
            
            if result.latency_ms is not None:
                latency = f"{result.latency_ms:.2f} ms"
        
            else:
                latency = "N/A"
            
        else:
            status = "[red]OFFLINE[/red]"
            latency = "--"
            
        table.add_row(
            result.host,
            status,
            latency,
        )
    # Print the completed table AFTER the loop
    console.print(table)
        
if __name__ == "__main__":
    main()



    
