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


        videos = list(
            self.config.videos_dir.glob(
                "*"
            )
        )


        if not videos:
            self.logger.warning(
                "No videos found."
            )

            return


        for video in videos:

            self.extract_video(
                video
            )



    def extract_video(
        self,
        video_path: Path,
    ) -> None:
        """
        Extract frames from one video.
        """

        self.logger.info(
            "Processing %s",
            video_path.name
        )


        capture = cv2.VideoCapture(
            str(video_path)
        )


        if not capture.isOpened():

            self.logger.error(
                "Cannot open %s",
                video_path
            )

            return



        fps = capture.get(
            cv2.CAP_PROP_FPS
        )

        total_frames = int(
            capture.get(
                cv2.CAP_PROP_FRAME_COUNT
            )
        )


        duration = total_frames / fps



        timestamps = (
            self.generate_timestamps(
                duration
            )
        )


        for index, timestamp in enumerate(
            timestamps
        ):

            frame_number = int(
                timestamp * fps
            )


            capture.set(
                cv2.CAP_PROP_POS_FRAMES,
                frame_number
            )


            success, frame = (
                capture.read()
            )


            if not success:
                continue



            filename = (
                f"{video_path.stem}_"
                f"{index:06d}."
                f"{self.config.image_format}"
            )


            output = (
                self.config.output_dir /
                filename
            )


            cv2.imwrite(
                str(output),
                frame,
            )


        capture.release()


        self.logger.info(
            "Finished %s",
            video_path.name
        )



    def generate_timestamps(
        self,
        duration: float,
    ) -> list[float]:
        """
        Generates frame timestamps.
        """

        mode = self.config.mode


        if mode == "random":

            return sorted(
                random.uniform(
                    0,
                    duration
                )
                for _ in range(
                    self.config.frames_per_video
                )
            )


        if mode == "uniform":

            step = (
                duration /
                self.config.frames_per_video
            )

            return [
                i * step
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