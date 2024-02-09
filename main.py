# This script executes the data ingestion stage of a Convolutional Neural Network (CNN) classifier training pipeline.
# It imports necessary modules, initializes logging, and executes data ingestion tasks.

from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage03_model_trainer import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage04_model_evaluation import EvaluationPipeline


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



STAGE_NAME = "Prepare base model"
# Try-except block for Prepare Base Model Stage
try: 
    # Logging the start of the stage
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    # Creating an instance of PrepareBaseModelTrainingPipeline and calling its main method
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    # Logging the completion of the stage
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# Handling any exceptions and logging them
except Exception as e:
    logger.exception(e)
    raise e


# Define the name for the model training
STAGE_NAME = "Training"  # Define the current stage name

try: 
    # Log start of stage
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    # Initialize model training pipeline
    model_trainer = ModelTrainingPipeline()
    
    # Execute main training process
    model_trainer.main()
    
    # Log completion of stage
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    # Log any exceptions that occur
    logger.exception(e)
    # Raise the exception again to propagate it up the call stack
    raise e



# Define the name for the Evaluation stage
STAGE_NAME = "Evaluation stage"

try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e
