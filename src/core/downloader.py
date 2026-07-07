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
    Downloads videos from URLs listed in a text file.
    """

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.options = {
            "format": "bestvideo[vcodec*=avc1]+bestaudio/best",
            "merge_output_format": "mp4",
            "download_archive": str(self.output_dir / "downloaded.txt"),
            "outtmpl": str(self.output_dir / "%(id)s.%(ext)s"),
            "noplaylist": True,
        }

    def load_urls(self, url_file: Path) -> list[str]:
        with open(url_file, "r", encoding="utf-8") as file:
            return [
                line.strip()
                for line in file
                if line.strip() and not line.startswith("#")
            ]

    def download_video(self, url: str) -> Path:
        with yt_dlp.YoutubeDL(self.options) as ydl:
            info = ydl.extract_info(url, download=True)

        return self.output_dir / f"{info['id']}.mp4"

    def download_from_file(self, url_file: Path) -> list[Path]:
        videos = []

        for index, url in enumerate(self.load_urls(url_file), start=1):
            print(f"[{index}] {url}")

            try:
                videos.append(self.download_video(url))

            except Exception as error:
                print(f"Failed: {url}\n{error}")

        return videos
