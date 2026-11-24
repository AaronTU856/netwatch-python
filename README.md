# NetWatch Python

A lightweight command-line network monitoring and diagnostics toolkit built with Python.

NetWatch monitors configured hosts with ICMP ping checks, tests configured TCP ports, presents the current results in a Rich terminal table, and records host availability and latency history in SQLite.

This is a portfolio and learning project focused on practical Python, networking, monitoring, logging, testing, and automation.

## Features

- Continuous monitoring of configured hosts
- ICMP ping availability and latency checks
- TCP port availability checks
- JSON-based host configuration
- Rich terminal status table
- One-time scan mode
- Configurable refresh interval
- Rotating application logs
- SQLite history for host availability and latency
- Historical uptime, failure-count, and latency statistics
- Automated linting and tests with GitHub Actions

## Requirements

- Python 3.12 or later
- Network access to the hosts you choose to monitor

Use NetWatch only on systems and networks that you own or are explicitly authorised to administer.

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/AaronTU856/netwatch-python.git
cd netwatch-python
python3 -m venv .venv
source .venv/bin/activate
```

Install the project and its development dependencies:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

Create your local configuration from the included example:

```bash
cp config/hosts.example.json config/hosts.json
```

`config/hosts.json` is intentionally ignored by Git so that local addresses and monitoring choices are not committed.

## Configuration

NetWatch reads `config/hosts.json`. It must contain a positive integer `refresh_interval` and a list of hosts. Each host needs a `name` and `host`; `ports` is optional.

```json
{
  "refresh_interval": 10,
  "hosts": [
    {
      "name": "Local Router",
      "host": "192.168.1.1",
      "ports": [80, 443]
    },
    {
      "name": "Cloudflare DNS",
      "host": "1.1.1.1",
      "ports": [53, 443]
    }
  ]
}
```

## Usage

Start continuous monitoring:

```bash
netwatch
```

Run one scan and exit:

```bash
netwatch --once
```

Override the configured refresh interval for the current run:

```bash
netwatch --interval 30
```

Display the statistics collected in `data/netwatch.db`:

```bash
netwatch --stats
```

Use `Ctrl+C` to stop continuous monitoring.

### Runtime data

- Logs are written to `logs/netwatch.log` and rotate at 1 MB, retaining up to three backup files.
- Host check results are stored in `data/netwatch.db`.
- The statistics view groups results by configured host and shows checks, failures, uptime, average/minimum/maximum latency, and the latest check time.

## Testing and quality checks

Run the test suite:

```bash
pytest
```

Run the linter:

```bash
ruff check src tests
```

GitHub Actions runs both commands for pushes and pull requests targeting `main`.

## Project structure

```text
config/                  Local host configuration and committed example
src/netwatch/            Application package
  config.py              JSON configuration loading and validation
  ping.py                Cross-platform ping execution and latency parsing
  ports.py               TCP connectivity checks
  monitor.py             Status table, logging, and result persistence
  database.py            SQLite setup, storage, and aggregate queries
  statistics.py          Historical statistics table
  main.py                Command-line entry point
tests/                   Unit tests
```

## Future enhancements

The following are not currently implemented:

- Alert notifications
- DNS-specific checks
- REST API and web dashboard
- Containerised deployment
- Authentication, multi-user access, and remote configuration management

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Aaron Baggot — Computer Science graduate specialising in Security and Forensics.

GitHub: [AaronTU856](https://github.com/AaronTU856)
