# Python code for setting up logging configuration
import os
import sys
import logging

# Define the format string for logging messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory and filepath for storing log files
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure logging with a file handler and a stream handler
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger named "cnnClassifierLogger"
logger = logging.getLogger("cnnClassifierLogger")
