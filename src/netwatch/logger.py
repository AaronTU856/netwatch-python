import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(
    log_file: str | Path = "logs/netwatch.log",
    level: int = logging.INFO,
    logger_name: str = "netwatch",
) -> logging.Logger:
    """Create and configure the NetWatch application logger."""

    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger