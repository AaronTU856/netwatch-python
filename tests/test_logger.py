import logging

from netwatch.logger import setup_logger


def test_setup_logger_creates_log_file(tmp_path):
    log_file = tmp_path / "test.log"

    logger = setup_logger(
        log_file=log_file,
        level=logging.INFO,
        logger_name="netwatch_test_create",
    )

    logger.info("test message")

    for handler in logger.handlers:
        handler.flush()

    assert log_file.exists()


def test_logger_writes_message(tmp_path):
    log_file = tmp_path / "test.log"

    logger = setup_logger(
        log_file=log_file,
        level=logging.INFO,
        logger_name="netwatch_test_write",
    )

    logger.info("structured logging test")

    for handler in logger.handlers:
        handler.flush()

    contents = log_file.read_text(encoding="utf-8")

    assert "structured logging test" in contents