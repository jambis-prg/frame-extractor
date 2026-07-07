"""
Global constants for the Frame Extractor project.

This module contains fixed values used across the application.

Author:
    João Victor Nascimento Lima
"""

from pathlib import Path


# ============================================================
# Project Information
# ============================================================

PROJECT_NAME: str = "frame-extractor"

PROJECT_VERSION: str = "1.0.0"


# ============================================================
# Default Paths
# ============================================================

DEFAULT_CONFIG_FILE: Path = Path("config.yaml")

DEFAULT_VIDEOS_DIR: Path = Path("videos")

DEFAULT_URLS_FILE: Path = Path("urls_file.txt")

DEFAULT_OUTPUT_DIR: Path = Path("dataset/images")

DEFAULT_METADATA_FILE: Path = Path(
    "dataset/metadata.csv"
)

DEFAULT_LOG_FILE: Path = Path(
    "logs/extractor.log"
)


# ============================================================
# Supported Video Extensions
# ============================================================

SUPPORTED_VIDEO_EXTENSIONS: tuple[str, ...] = (
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".webm",
    ".mpg",
    ".mpeg",
)


# ============================================================
# Supported Image Formats
# ============================================================

SUPPORTED_IMAGE_FORMATS: tuple[str, ...] = (
    "jpg",
    "jpeg",
    "png",
)


DEFAULT_IMAGE_FORMAT: str = "jpg"


# ============================================================
# Extraction Modes
# ============================================================

MODE_RANDOM: str = "random"

MODE_UNIFORM: str = "uniform"

MODE_INTERVAL: str = "interval"


SUPPORTED_EXTRACTION_MODES: tuple[str, ...] = (
    MODE_RANDOM,
    MODE_UNIFORM,
    MODE_INTERVAL,
)


# ============================================================
# Default Extraction Parameters
# ============================================================

DEFAULT_FRAMES_PER_VIDEO: int = 300

DEFAULT_RANDOM_SEED: int = 42

DEFAULT_INTERVAL_SECONDS: float = 2.0

DEFAULT_MIN_TIME_BETWEEN_FRAMES: float = 1.5


# ============================================================
# Processing Parameters
# ============================================================

DEFAULT_WORKERS: int = 0

DEFAULT_IMAGE_QUALITY: int = 95


# ============================================================
# Metadata
# ============================================================

DEFAULT_METADATA_COLUMNS: tuple[str, ...] = (
    "image",
    "video",
    "frame",
    "timestamp",
    "width",
    "height",
)


# ============================================================
# Logging
# ============================================================

LOG_FORMAT: str = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)


DEFAULT_LOG_LEVEL: str = "INFO"


# ============================================================
# File Naming
# ============================================================

IMAGE_NAME_PADDING: int = 6

DEFAULT_IMAGE_PREFIX: str = ""


# ============================================================
# OpenCV
# ============================================================

DEFAULT_VIDEO_CODEC: str = "mp4v"