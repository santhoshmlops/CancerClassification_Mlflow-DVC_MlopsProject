# Script for training a convolutional neural network (CNN) classifier.
# This script sets up a pipeline for training the model, including configuration,
# data loading, model initialization, training, and logging of progress and errors.

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger

# Define the stage name for logging purposes
STAGE_NAME = "Training"

# Class to manage the model training pipeline
class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Initialize configuration manager
        config = ConfigurationManager()
        # Retrieve training configuration
        training_config = config.get_training_config()
        # Initialize training object with configuration
        training = Training(config=training_config)
        # Initialize base model
        training.get_base_model()
        # Set up training and validation data generators
        training.train_valid_generator()
        # Train the model
        training.train()

if __name__ == '__main__':
    try:
        # Log start of the training stage
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # Initialize the training pipeline
        obj = ModelTrainingPipeline()
        # Execute the main training process
        obj.main()
        # Log completion of the training stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur during execution
        logger.exception(e)
        # Re-raise the exception to halt execution
        raise e
