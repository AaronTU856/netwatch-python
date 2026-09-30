import sqlite3
from pathlib import Path


def init_database(
    database_path: str | Path = "data/netwatch.db",
) -> None:
    """Create the NetWatch SQLite database and required tables."""

    path = Path(database_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS host_checks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                checked_at TEXT NOT NULL,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                reachable INTEGER NOT NULL,
                latency_ms REAL
            )
            """
        )

        connection.commit()


def save_host_check(
    checked_at: str,
    name: str,
    host: str,
    reachable: bool,
    latency_ms: float | None,
    database_path: str | Path = "data/netwatch.db",
) -> None:
    """Store a host monitoring result."""

    path = Path(database_path)

    with sqlite3.connect(path) as connection:
        connection.execute(
            """
            INSERT INTO host_checks (
                checked_at,
                name,
                host,
                reachable,
                latency_ms
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                checked_at,
                name,
                host,
                int(reachable),
                latency_ms,
            ),
        )

        connection.commit()
        
def get_host_statistics(
    database_path: str | Path = "data/netwatch.db",
) -> list[tuple]:
    """Return monitoring statistics grouped by host."""

    path = Path(database_path)

    with sqlite3.connect(path) as connection:
        cursor = connection.execute(
            """
            SELECT
                name,
                host,
                COUNT(*) AS total_checks,
                SUM(reachable) AS successful_checks,
                COUNT(*) - SUM(reachable) AS failed_checks,
                ROUND(
                    (SUM(reachable) * 100.0) / COUNT(*),
                    2
                ) AS uptime_percent,
                ROUND(AVG(latency_ms), 2) AS average_latency,
                ROUND(MIN(latency_ms), 2) AS minimum_latency,
                ROUND(MAX(latency_ms), 2) AS maximum_latency,
                MAX(checked_at) AS last_check
            FROM host_checks
            GROUP BY name, host
            ORDER BY name
            """
        )

        return cursor.fetchall()

