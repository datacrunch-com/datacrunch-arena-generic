import os

import joblib


def load_model(path):
    if not os.access(path, os.R_OK):
        print(f"argh... the file for the model {path} does not exists or is not readable, are you sure you put it in?")
        exit(1)
    
    return joblib.load(path)
