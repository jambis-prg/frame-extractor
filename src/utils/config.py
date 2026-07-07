"""
Configuration manager for Frame Extractor.

Loads YAML configuration files and exposes
settings through a typed Python object.

Author:
    João Victor Nascimento Lima
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from src.constants import (
    DEFAULT_CONFIG_FILE,
    DEFAULT_VIDEOS_DIR,
    DEFAULT_OUTPUT_DIR,
    DEFAULT_METADATA_FILE,
    DEFAULT_LOG_FILE,
    DEFAULT_IMAGE_FORMAT,
    DEFAULT_FRAMES_PER_VIDEO,
    DEFAULT_RANDOM_SEED,
    DEFAULT_WORKERS,
    DEFAULT_INTERVAL_SECONDS,
    DEFAULT_MIN_TIME_BETWEEN_FRAMES,
    DEFAULT_IMAGE_QUALITY,
    DEFAULT_METADATA_COLUMNS,
)


@dataclass
class Config:
    """
    Application configuration.

    Attributes
    ----------
    videos_dir:
        Directory containing input videos.

    output_dir:
        Directory where extracted frames are saved.

    metadata_file:
        CSV metadata output path.
    """

    videos_dir: Path = DEFAULT_VIDEOS_DIR

    output_dir: Path = DEFAULT_OUTPUT_DIR

    metadata_file: Path = DEFAULT_METADATA_FILE

    log_file: Path = DEFAULT_LOG_FILE


    mode: str = "random"

    frames_per_video: int = DEFAULT_FRAMES_PER_VIDEO

    random_seed: int = DEFAULT_RANDOM_SEED

    interval_seconds: float = DEFAULT_INTERVAL_SECONDS

    min_time_between_frames: float = (
        DEFAULT_MIN_TIME_BETWEEN_FRAMES
    )


    workers: int = DEFAULT_WORKERS


    image_format: str = DEFAULT_IMAGE_FORMAT

    image_quality: int = DEFAULT_IMAGE_QUALITY


    overwrite: bool = False

    continue_numbering: bool = True


    verbose: bool = True

    save_logs: bool = True

    save_metadata: bool = True


    metadata_columns: tuple[str, ...] = field(
        default_factory=lambda: DEFAULT_METADATA_COLUMNS
    )


    @classmethod
    def load(cls, path: Path = DEFAULT_CONFIG_FILE) -> "Config":
        """
        Loads configuration from YAML file.
        """

        if not path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {path}"
            )


        with open(path, "r", encoding="utf-8") as file:
            data: dict[str, Any] = yaml.safe_load(file) or {}


        return cls(
            videos_dir=Path(
                data.get(
                    "videos_dir",
                    DEFAULT_VIDEOS_DIR
                )
            ),

            output_dir=Path(
                data.get(
                    "output_dir",
                    DEFAULT_OUTPUT_DIR
                )
            ),

            metadata_file=Path(
                data.get(
                    "metadata_file",
                    DEFAULT_METADATA_FILE
                )
            ),

            log_file=Path(
                data.get(
                    "log_file",
                    DEFAULT_LOG_FILE
                )
            ),

            mode=data.get(
                "mode",
                "random"
            ),

            frames_per_video=data.get(
                "frames_per_video",
                DEFAULT_FRAMES_PER_VIDEO
            ),

            random_seed=data.get(
                "random_seed",
                DEFAULT_RANDOM_SEED
            ),

            interval_seconds=data.get(
                "interval_seconds",
                DEFAULT_INTERVAL_SECONDS
            ),

            min_time_between_frames=data.get(
                "min_time_between_frames",
                DEFAULT_MIN_TIME_BETWEEN_FRAMES
            ),

            workers=data.get(
                "workers",
                DEFAULT_WORKERS
            ),

            image_format=data.get(
                "image_format",
                DEFAULT_IMAGE_FORMAT
            ),

            image_quality=data.get(
                "image_quality",
                DEFAULT_IMAGE_QUALITY
            ),

            overwrite=data.get(
                "overwrite",
                False
            ),

            continue_numbering=data.get(
                "continue_numbering",
                True
            ),

            verbose=data.get(
                "verbose",
                True
            ),

            save_logs=data.get(
                "save_logs",
                True
            ),

            save_metadata=data.get(
                "save_metadata",
                True
            ),

            metadata_columns=tuple(
                data.get(
                    "metadata_columns",
                    DEFAULT_METADATA_COLUMNS
                )
            ),
        )


    def create_directories(self) -> None:
        """
        Creates required project directories.
        """

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.metadata_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )