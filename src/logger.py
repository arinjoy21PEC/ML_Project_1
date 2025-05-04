import logging
import os
from datetime import datetime

"""
This script sets up a logging system that:
1. Creates a 'logs' directory in the current working directory if it doesn't already exist.
2. Generates a log file with the current date and time in its name.
3. Configures the logging module to write logs to that file, including timestamp, line number, logger name, log level, and message.
"""

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
