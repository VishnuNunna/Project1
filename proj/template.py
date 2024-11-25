import os
from pathlib import Path

list_of_files = [
    "Analysis/Data/.gitkeep",
    "Analysis/Exploratoey_Data_Analysis.ipynb",
    "Analysis/Model_Training.ipynb",
    "core/__init__.py",
    "core/exception.py",
    "core/logger.py",
    "core/utils.py",
    "core/components/__init__.py",
    "core/components/Data_ingestion.py",
    "core/components/Data_transformation.py",
    "core/components/Model_trainer.py",
    "core/pipeline/__init__.py",
    "core/pipeline/Prediction_pipeline.py",
    "core/pipeline/Training_pipeline.py",
    "static/styles.css",
    "templates/home.html",
    ".gitignore",
    "app.py",
    "requirements.txt",
    "setup.py"]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
