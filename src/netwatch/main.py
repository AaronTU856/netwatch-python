import argparse
import time
from pathlib import Path

from rich.console import Console

from netwatch.config import load_config
from netwatch.database import init_database
from netwatch.logger import setup_logger
from netwatch.monitor import build_status_table, get_timestamp
from netwatch.statistics import build_statistics_table

console = Console()
logger = setup_logger()

CONFIG_PATH = Path("config/hosts.json")



def main() -> None:
    """Run the NetWatch continueous monitoring application."""
    
    args = parse_arguments()
    
    
    try:
        config = load_config(CONFIG_PATH)
    except (FileNotFoundError, ValueError) as error:
        console.print(f"[red]Configuration error:[/red] {error}")
        return
    
    init_database()
    
    if args.stats:
        console.print()
        console.print(build_statistics_table())
        return
    logger.info(
        "netwatch_started refresh_interval=%s host_count=%s",
        config.refresh_interval,
        len(config.hosts),
    )
    
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
        
            logger.info(
            "netwatch_started refresh_interval=%s host_count=%s",
            config.refresh_interval,
            len(config.hosts),
        )
    
    except KeyboardInterrupt:
        logger.info("netwatch_stopped")
        
        console.print()
        console.print()
        console.print("[yellow]NetWatch stopped.[/yellow]")
        
def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="NetWatch network monitoring toolkit"
    )

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Display historical monitoring statistics",
    )

    return parser.parse_args()

    
if __name__ == "__main__":
    main()



    
