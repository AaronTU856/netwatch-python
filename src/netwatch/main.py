import time
from pathlib import Path

from rich.console import Console

from netwatch.config import load_config
from netwatch.monitor import build_status_table, get_timestamp

console = Console()

CONFIG_PATH = Path("config/hosts.json")


def main() -> None:
    """Run the NetWatch continueous monitoring application."""
    
    try:
        config = load_config(CONFIG_PATH)
    except (FileNotFoundError, ValueError) as error:
        console.print(f"[red]Configuration error:[/red] {error}")
        return
    
    try:
        while True:
            console.clear()
            
        
            console.print("[bold cyan]NetWatch Python[/bold cyan]")
            console.print("Network monitoring and diagnostics toolkit")
            console.print()
            
            console.print(
                f"Last scan: [bold]{get_timestamp()}[/bold]"
                
            )
            console.print(
                f"refresh interval: "
                f"[bold]{config.refresh_interval} seconds[/bold]"
            )
            console.print()
            
            table = build_status_table(config.hosts)
            
            console.print(table)
            
            console.print()
            console.print(
                "[dim]Press Ctrl + C to stop NetWatch[/dim]"
                
            )
            
            time.sleep(config.refresh_interval)
        
    except KeyboardInterrupt:
        console.print()
        console.print()
        console.print("[yellow]NetWatch stopped.[/yellow]")
    
    
        
if __name__ == "__main__":
    main()



    
