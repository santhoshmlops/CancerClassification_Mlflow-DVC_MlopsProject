# Configuration Manager for CNN Classifier

import os
from cnnClassifier.constant import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig)                                       
                                                
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        # Initialize with configuration and parameters file paths
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create necessary directories
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieves data ingestion configuration.

        Returns:
            DataIngestionConfig: Object containing data ingestion configuration.
        """
        config = self.config.data_ingestion

        # Create directories specified in the data ingestion configuration
        create_directories([config.root_dir])

        # Construct and return DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

    # Method to retrieve and prepare configuration settings for the base model
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        """
        Retrieves and prepares configuration settings for the base model.

        Returns:
            PrepareBaseModelConfig: Configuration object for preparing the base model.
        """
        config = self.config.prepare_base_model
    
        # Create directories based on the configuration's root directory
        create_directories([config.root_dir])

        # Create PrepareBaseModelConfig object with relevant parameters
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config

    


