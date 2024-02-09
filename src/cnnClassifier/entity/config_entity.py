from dataclasses import dataclass
from pathlib import Path

# Define a data class to hold configuration parameters for data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    # Root directory where the data will be stored or ingested from
    root_dir: Path
    
    # URL from which the data will be fetched
    source_URL: str
    
    # Local file path where the data will be stored after ingestion
    local_data_file: Path
    
    # Directory where the data will be unzipped if it's compressed
    unzip_dir: Path


# Defining a data class for configuring base model preparation
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    # Root directory where the base model and updates are stored
    root_dir: Path
    
    # Path to the base model
    base_model_path: Path
    
    # Path to store the updated base model
    updated_base_model_path: Path
    
    # Parameters related to image size (e.g., width, height)
    params_image_size: list
    
    # Learning rate parameter for the model
    params_learning_rate: float
    
    # Boolean indicating whether to include top layers in the model
    params_include_top: bool
    
    # String representing the weights parameter
    params_weights: str
    
    # Number of classes in the model
    params_classes: int