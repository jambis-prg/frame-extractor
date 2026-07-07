"""
Entry point for the Frame Extractor application.

This module allows the project to be executed using:

    python -m src

Author:
    João Victor Nascimento Lima
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src import __version__
from src.core.pipeline import DatasetPipeline
from src.utils.config import Config
from src.utils.logger import setup_logger


def build_parser() -> argparse.ArgumentParser:
    """
    Creates and configures the command-line argument parser.
    """

    parser = argparse.ArgumentParser(
        prog="frame-extractor",
        description=(
            "Automatic video dataset generation "
            "and frame extraction tool."
        ),
    )


    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        default=Path("config.yaml"),
        help="Path to configuration YAML file.",
    )


    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )


    return parser



def main() -> int:
    """
    Application entry point.
    """

    parser = build_parser()
    args = parser.parse_args()


    try:
        config = Config.load(
            args.config
        )


        logger = setup_logger(
            config
        )


        logger.info("=" * 60)
        logger.info("Frame Extractor")
        logger.info("Version: %s", __version__)
        logger.info("=" * 60)


        pipeline = DatasetPipeline(
            config,
            logger
        )


        pipeline.run()


        logger.info(
            "Execution completed successfully."
        )


        return 0


    except KeyboardInterrupt:

        print(
            "\nInterrupted by user."
        )

        return 130


    except Exception as exc:

        print(
            f"\nFatal error: {exc}"
        )

        return 1



if __name__ == "__main__":
    sys.exit(main())