# This script executes the data ingestion stage of a Convolutional Neural Network (CNN) classifier training pipeline.
# It imports necessary modules, initializes logging, and executes data ingestion tasks.

from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

# Define the name for the data ingestion stage
STAGE_NAME = "Data Ingestion stage"

try:
    # Log start of the data ingestion stage
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    # Instantiate DataIngestionTrainingPipeline object
    obj = DataIngestionTrainingPipeline()
    
    # Execute the main method of the pipeline object
    obj.main()
    
    # Log completion of the data ingestion stage
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    # Log exception and raise it
    logger.exception(e)
    raise e
