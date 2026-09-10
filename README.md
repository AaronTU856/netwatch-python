# NetWatch Python

A lightweight network monitoring and diagnostics toolkit built with Python.

NetWatch is a personal portfolio and learning project designed to explore practical networking, monitoring, automation and cybersecurity concepts using Python.

## Project Goals

NetWatch will provide tools for monitoring hosts and network services while presenting results through an easy-to-use command-line interface.

Planned capabilities include:

- Host availability monitoring
- ICMP/ping latency checks
- TCP port availability checks
- Configurable network hosts
- Structured logging
- Historical monitoring data
- Terminal dashboard
- Network statistics
- Alerting
- REST API
- Web dashboard
- Docker deployment

## Current Status

**Version: 0.1.0 — Initial Development**

The project structure and development environment are currently being established.

## Planned Architecture

```text
Network Hosts
      |
      v
Monitoring Engine
      |
      +---- Ping checks
      |
      +---- TCP checks
      |
      +---- DNS checks
      |
      v
Result Processing
      |
      +---- Terminal UI
      +---- Logging
      +---- Database
      |
      v
Future REST API / Web Dashboard
```

## Technology

- Python
- Rich
- Pytest

Future technologies may include:

- FastAPI
- SQLite/PostgreSQL
- Docker
- GitHub Actions
- Raspberry Pi
- Cloud deployment

## Installation

Clone the repository:

```bash
git clone https://github.com/AaronTU856/netwatch-python.git
cd netwatch-python
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run NetWatch:

```bash
python src/netwatch/main.py
```

## Testing

Run the test suite with:

```bash
pytest
```

## Roadmap

### v0.1
- Initial project structure
- Host configuration
- Ping monitoring
- TCP port checks
- Terminal output

### v0.2
- Structured logging
- Continuous monitoring
- Improved terminal dashboard

### v0.3
- SQLite monitoring history
- Statistics and reporting

### v0.4
- FastAPI REST API

### v0.5
- Web dashboard

### v1.0
- Stable monitoring application
- Documentation
- Docker support
- Automated tests and CI

## Security

NetWatch is intended for monitoring systems and networks that the user owns or is explicitly authorised to administer.

No credentials, local network configuration or private environment files should be committed to this repository.

## Author

**Aaron Baggot**

Computer Science graduate specialising in Security and Forensics.

GitHub: [AaronTU856](https://github.com/AaronTU856)

## License

This project is licensed under the MIT License.
