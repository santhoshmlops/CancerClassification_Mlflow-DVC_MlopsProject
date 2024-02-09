# Script for training pipeline to prepare a Convolutional Neural Network (CNN) classifier's base model

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

# Constants
STAGE_NAME = "Prepare base model"

# Class definition for training pipeline
class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    # Main functionality of the pipeline
    def main(self):
        # Initialize configuration manager
        config = ConfigurationManager()
        # Retrieve configuration for preparing the base model
        prepare_base_model_config = config.get_prepare_base_model_config()
        # Initialize PrepareBaseModel instance with obtained configuration
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        # Get the base model
        prepare_base_model.get_base_model()
        # Update the base model (e.g., fine-tuning)
        prepare_base_model.update_base_model()

# Main block
if __name__ == '__main__':
    try:
        # Log start of the stage
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # Initialize and execute the pipeline
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        # Log completion of the stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log exceptions and raise further
        logger.exception(e)
        raise e
