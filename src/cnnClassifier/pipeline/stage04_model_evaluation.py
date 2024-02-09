# Import necessary modules and classes
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import Evaluation
from cnnClassifier import logger

# Define a constant for the stage name
STAGE_NAME = "Evaluation stage"

# Define a class representing the evaluation pipeline
class EvaluationPipeline:
    def __init__(self):
        pass

    # Method representing the main logic of the evaluation pipeline
    def main(self):
        # Fetch configuration settings
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        
        # Initialize evaluation object with configuration
        evaluation = Evaluation(eval_config)
        
        # Perform evaluation
        evaluation.evaluation()
        
        # Save evaluation scores
        evaluation.save_score()
        
        # Optionally log into MLflow
        evaluation.log_into_mlflow()

# Main block of the script
if __name__ == '__main__':
    try:
        # Log the start of the evaluation stage
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Instantiate and run the EvaluationPipeline
        obj = EvaluationPipeline()
        obj.main()
        
        # Log the completion of the evaluation stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    # Catch any exceptions, log them, and re-raise
    except Exception as e:
        logger.exception(e)
        raise e
