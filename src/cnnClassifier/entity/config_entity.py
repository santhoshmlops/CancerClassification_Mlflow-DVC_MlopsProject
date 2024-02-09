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
