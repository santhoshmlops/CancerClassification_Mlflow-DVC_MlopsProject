import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from cnnClassifier.entity.config_entity import EvaluationConfig  # Importing necessary modules and libraries
from cnnClassifier.utils.common import read_yaml, create_directories, save_json

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config  # Initializing the Evaluation class with an instance of EvaluationConfig
    
    def _valid_generator(self):
        # Setting up data generator for validation data
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)  # Static method to load a Keras model from a given path
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)  # Loading the model
        self._valid_generator()  # Setting up the validation data generator
        self.score = self.model.evaluate(self.valid_generator)  # Evaluating the model
        self.save_score()  # Saving the evaluation scores
    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}  # Constructing a dictionary of scores
        save_json(path=Path("scores.json"), data=scores)  # Saving the scores into a JSON file
    
    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)  # Setting MLflow registry URI
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme  # Getting the tracking URL type

        with mlflow.start_run():  # Starting an MLflow run
            mlflow.log_params(self.config.all_params)  # Logging parameters
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}  # Logging evaluation metrics
            )
            if tracking_url_type_store != "file":  # Checking if MLflow is not using a file store
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")  # Logging the model with a registered model name
            else:
                mlflow.keras.log_model(self.model, "model")  # Logging the model without a registered model name
