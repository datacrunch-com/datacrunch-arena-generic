import os

import pickle


def load_model(path):
    """
    Load a model with joblib, but check if the file exists first.
    This is to print a more friendly message.
    
    Parameters
    ----------
    path : str
        File path to check.
    
    Returns
    -------
    joblib.load(path)
    
    Notes
    -----
    Aside from check if the file is readable, nothing else is done.
    """
    if not os.access(path, os.R_OK):
        print(f"argh... the file for the model {path} does not exists or is not readable, are you sure you put it in?")
        exit(1)
    
    with open(path, "rb") as fd:
        return pickle.load(fd)
