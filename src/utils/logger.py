"""
Logging configuration.

Author:
    João Victor Nascimento Lima
"""

from __future__ import annotations

import logging
from pathlib import Path

from src.constants import (
    LOG_FORMAT,
    DEFAULT_LOG_LEVEL,
)

from src.utils.config import Config



def setup_logger(
    config: Config,
) -> logging.Logger:
    """
    Creates application logger.
    """

    logger = logging.getLogger(
        "frame-extractor"
    )

    logger.setLevel(
        getattr(
            logging,
            DEFAULT_LOG_LEVEL
        )
    )


    if logger.handlers:
        return logger


    formatter = logging.Formatter(
        LOG_FORMAT
    )


    console = logging.StreamHandler()

    console.setFormatter(
        formatter
    )

    logger.addHandler(
        console
    )


    if config.save_logs:

        config.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        file_handler = logging.FileHandler(
            config.log_file,
            encoding="utf-8"
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )


    return logger