# Script for data ingestion stage in a Convolutional Neural Network (CNN) training pipeline.

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

# Constant defining the name of the data ingestion stage
STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Get configuration manager
        config = ConfigurationManager()
        # Get data ingestion configuration
        data_ingestion_config = config.get_data_ingestion_config()
        # Create DataIngestion object with configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # Download file
        data_ingestion.download_file()
        # Extract downloaded zip file
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        # Log start of data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # Create instance of DataIngestionTrainingPipeline and call main method
        obj = DataIngestionTrainingPipeline()
        obj.main()
        # Log completion of data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur during execution
        logger.exception(e)
        raise e
