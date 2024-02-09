import os
import zipfile
import gdown
import logging
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Caption: Download File Method
        Description: Fetches data from the URL provided in the configuration and saves it to the local file system.
        Returns the path of the downloaded file.
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            
            gdown.download(dataset_url, zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
            return zip_download_dir
        except Exception as e:
            logger.error(f"Error occurred during file download: {e}")
            raise

    def extract_zip_file(self):
        """
        Caption: Extract Zip File Method
        Description: Extracts the contents of the downloaded zip file into the specified directory.
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted contents of the zip file to {unzip_path}")
        except Exception as e:
            logger.error(f"Error occurred during zip file extraction: {e}")
            raise
