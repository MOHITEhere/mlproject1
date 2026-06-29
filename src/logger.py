'''Purpose

Stores logs of what the application is doing.

Instead of printing

print("Data Loaded")

you write

logging.info("Data Loaded")

The output is saved to a log file.

Example:

10:15:20

Data Loaded

↓

10:15:21

Data Split Completed

↓

10:15:25

Model Training Started

↓

10:15:40

Model Saved

Simple meaning:

Keeps a permanent record
of the application's execution.'''

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)


