from rich.table import Table

from netwatch.database import get_host_statistics


def build_statistics_table() -> Table:
    """Build a Rich table containing historical host statistics."""

    rows = get_host_statistics()

    table = Table(title="NetWatch Statistics")

    table.add_column("Name")
    table.add_column("Host")
    table.add_column("Checks", justify="right")
    table.add_column("Failures", justify="right")
    table.add_column("Uptime", justify="right")
    table.add_column("Avg Latency", justify="right")
    table.add_column("Min", justify="right")
    table.add_column("Max", justify="right")
    table.add_column("Last Check")

    for row in rows:
        (
            name,
            host,
            total_checks,
            _successful_checks,
            failed_checks,
            uptime_percent,
            average_latency,
            minimum_latency,
            maximum_latency,
            last_check,
        ) = row

        table.add_row(
            name,
            host,
            str(total_checks),
            str(failed_checks),
            f"{uptime_percent:.2f}%",
            (
                f"{average_latency:.2f} ms"
                if average_latency is not None
                else "N/A"
            ),
            (
                f"{minimum_latency:.2f} ms"
                if minimum_latency is not None
                else "N/A"
            ),
            (
                f"{maximum_latency:.2f} ms"
                if maximum_latency is not None
                else "N/A"
            ),
            last_check,
        )

    return table