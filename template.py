import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = 'TextSummarizer'

list_of_files = [
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

for filepath in list_of_files:
    '''
    Path function help to construct pure file path and it is automatically detected the OS and 
    convert the file path based on the OS standard (windows, linux, ubuntu etc...)
    '''
    filepath = Path(filepath)
    # create the directory and filename : split the filepath into fiename and file dirctory
    filedir, filename = os.path.split(filepath) 

    # check if the directory and folder exists. if it does not then create
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating dirctory: {filedir} for the file: {filepath}")

    # check the filepath exist or not :- if not then create 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file {filepath}")

    else:
        logging.info(f"file : {filepath} already exist")