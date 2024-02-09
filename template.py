# Importing necessary modules
import os
from pathlib import Path
import logging

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s:')

# Defining variables
project_name = "cnnClassifier"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py"
]

# Iterating through list of files
for filepath in list_of_files:
    # Convert file path to a Path object
    filepath = Path(filepath)
    # Extract directory and filename
    filedir, filename = filepath.parent, filepath.name

    # Creating directories if necessary
    if filedir != "":
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating File Directory: {filedir} for the file {filename}")

    # Creating empty files if they don't exist
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating Empty File: {filepath}")
    else:
        # Logging if file already exists
        logging.info(f"{filename} already exists")
