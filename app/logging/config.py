"""Logging configuration with coloredlogs support."""

import logging

import coloredlogs


def setup_logging(
    level: str = "INFO",
    logger_name: str | None = None,
    format_string: str | None = None,
    milliseconds: bool = True,
) -> logging.Logger:
    """
    Setup colored logging for the application.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        logger_name: Name of the logger. If None, uses root logger
        format_string: Custom log format. If None, uses default format
        milliseconds: Whether to include milliseconds in timestamps

    Returns:
        Configured logger instance
    """
    # Default format with clean, readable output
    if format_string is None:
        format_string = "%(asctime)s %(name)s %(levelname)s %(message)s"

    # Get or create logger
    if logger_name:
        logger = logging.getLogger(logger_name)
    else:
        logger = logging.getLogger()

    # Install coloredlogs
    coloredlogs.install(
        level=level, logger=logger, fmt=format_string, milliseconds=milliseconds
    )

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the given name.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Logger instance
    """
    return logging.getLogger(name)
