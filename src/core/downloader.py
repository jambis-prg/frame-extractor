"""
Video downloader module.

Downloads videos from a list of URLs.

Author:
    João Victor Nascimento Lima
"""

from pathlib import Path

import yt_dlp


class VideoDownloader:
    """
    Downloads videos from a list of URLs.
    """

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.options = {
            "format": "bestvideo",
            "download_archive": str(
                self.output_dir / "downloaded.txt"
            ),
            "outtmpl": str(
                self.output_dir / "%(id)s.%(ext)s"
            ),
            "noplaylist": True,
            "ignoreerrors": True,
            "retries": 10,
            "fragment_retries": 10,
            "quiet": True,
            "no_warnings": True,
        }

    @staticmethod
    def load_urls(url_file: Path) -> list[str]:
        """
        Loads URLs from a text file.
        """

        return [
            line.strip()
            for line in url_file.read_text(
                encoding="utf-8"
            ).splitlines()
            if line.strip() and not line.startswith("#")
        ]

    def download_video(
        self,
        ydl: yt_dlp.YoutubeDL,
        url: str,
    ) -> Path | None:
        """
        Downloads one video.
        """

        info = ydl.extract_info(
            url,
            download=True,
        )

        if info is None:
            return None

        return (
            self.output_dir /
            f"{info['id']}.{info['ext']}"
        )

    def download_from_file(
        self,
        url_file: Path,
    ) -> list[Path]:
        """
        Downloads all videos listed in a file.
        """

        videos: list[Path] = []

        urls = self.load_urls(url_file)

        with yt_dlp.YoutubeDL(self.options) as ydl:

            for index, url in enumerate(
                urls,
                start=1,
            ):

                print(
                    f"[{index}/{len(urls)}] {url}"
                )

                try:
                    video = self.download_video(
                        ydl,
                        url,
                    )

                    if video is not None:
                        videos.append(video)

                except Exception as error:
                    print(
                        f"Failed to download:\n"
                        f"{url}\n"
                        f"{error}"
                    )

        return videos