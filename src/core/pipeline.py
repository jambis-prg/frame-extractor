from src.core.downloader import VideoDownloader
from src.core.extractor import FrameExtractor


class DatasetPipeline:

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger


    def run(self):

        downloader = VideoDownloader(
            self.config.videos_dir
        )

        videos = downloader.download_from_file(
            self.config.urls_file
        )

        self.logger.info(
            "Downloaded %d videos.",
            len(videos)
        )

        extractor = FrameExtractor(
            self.config,
            self.logger
        )

        extractor.run()

        self.logger.info(
            "Pipeline completed."
        )