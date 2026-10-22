"""
Video frame extraction engine.

Author:
    João Victor Nascimento Lima
"""

from __future__ import annotations

import random

from pathlib import Path
from logging import Logger

import cv2

from src.utils.config import Config


VIDEO_EXTENSIONS = {
    ".mp4",
    ".mkv",
    ".webm",
    ".mov",
    ".avi",
}


class FrameExtractor:
    """
    Extracts frames from videos.
    """

    def __init__(
        self,
        config: Config,
        logger: Logger,
    ) -> None:

        self.config = config
        self.logger = logger

        random.seed(
            config.random_seed
        )

    def run(self) -> None:
        """
        Starts extraction process.
        """

        self.config.create_directories()

        videos = sorted(
            video
            for video in self.config.videos_dir.iterdir()
            if video.is_file()
            and video.suffix.lower() in VIDEO_EXTENSIONS
        )

        if not videos:
            self.logger.warning(
                "No videos found."
            )
            return

        for video in videos:
            self.extract_video(video)

    def extract_video(
        self,
        video_path: Path,
    ) -> None:
        """
        Extract frames from one video.
        """

        self.logger.info(
            "Processing %s",
            video_path.name,
        )

        capture = cv2.VideoCapture(
            str(video_path)
        )

        if not capture.isOpened():

            self.logger.error(
                "Cannot open %s",
                video_path,
            )

            return

        try:

            fps = capture.get(
                cv2.CAP_PROP_FPS
            )

            total_frames = int(
                capture.get(
                    cv2.CAP_PROP_FRAME_COUNT
                )
            )

            if fps <= 0:

                self.logger.error(
                    "Invalid FPS for %s",
                    video_path.name,
                )

                return

            if total_frames <= 0:

                self.logger.error(
                    "Video contains no frames: %s",
                    video_path.name,
                )

                return

            width = int(
                capture.get(
                    cv2.CAP_PROP_FRAME_WIDTH
                )
            )

            height = int(
                capture.get(
                    cv2.CAP_PROP_FRAME_HEIGHT
                )
            )

            duration = total_frames / fps

            self.logger.info(
                "Resolution: %dx%d | FPS: %.2f | Duration: %.1fs",
                width,
                height,
                fps,
                duration,
            )

            timestamps = self.generate_timestamps(
                duration
            )

            frame_targets = sorted(
                {
                    min(
                        int(timestamp * fps),
                        total_frames - 1,
                    )
                    for timestamp in timestamps
                }
            )

            if not frame_targets:
                return

            params = []

            if (
                self.config.image_format.lower()
                in {"jpg", "jpeg"}
            ):

                params = [
                    cv2.IMWRITE_JPEG_QUALITY,
                    100,
                ]

            current_target = 0
            current_frame = 0
            saved = 0

            success, frame = capture.read()

            while (
                success
                and current_target < len(frame_targets)
            ):

                target = frame_targets[current_target]

                if current_frame == target:

                    filename = (
                        f"{video_path.stem}_"
                        f"{saved:06d}."
                        f"{self.config.image_format}"
                    )

                    output = (
                        self.config.output_dir
                        / filename
                    )

                    ok = cv2.imwrite(
                        str(output),
                        frame,
                        params,
                    )

                    if not ok:

                        self.logger.warning(
                            "Failed to save %s",
                            output.name,
                        )

                    else:

                        saved += 1

                    current_target += 1

                success, frame = capture.read()

                current_frame += 1

            self.logger.info(
                "Saved %d frame(s) from %s",
                saved,
                video_path.name,
            )

        finally:

            capture.release()

    def generate_timestamps(
        self,
        duration: float,
    ) -> list[float]:
        """
        Generates frame timestamps.
        """

        mode = self.config.mode

        if mode == "random":

            segment = (
                duration /
                self.config.frames_per_video
            )

            return sorted(
                random.uniform(
                    i * segment,
                    (i + 1) * segment,
                )
                for i in range(
                    self.config.frames_per_video
                )
            )

        if mode == "uniform":

            step = (
                duration /
                (
                    self.config.frames_per_video
                    + 1
                )
            )

            return [
                (i + 1) * step
                for i in range(
                    self.config.frames_per_video
                )
            ]

        if mode == "interval":

            timestamps = []

            current = 0.0

            while current < duration:

                timestamps.append(
                    current
                )

                current += (
                    self.config.interval_seconds
                )

            return timestamps

        raise ValueError(
            f"Unknown extraction mode: {mode}"
        )