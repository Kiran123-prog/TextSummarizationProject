import os
from pathlib import Path
import logging

# setting up the loggig structure
logging.basicConfig(level=logging.info, format='[%(asctime)s] %(message)s')

# define the project name
project_name = 'Text Summarization'

# list of files that wnat to create, it need for this project
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py"
]

