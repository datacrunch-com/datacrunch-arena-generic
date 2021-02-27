import json

import pandas

import helper


model_r = helper.load_model("data/model_target_r")
model_g = helper.load_model("data/model_target_g")
model_b = helper.load_model("data/model_target_b")


def do(features):
    """
    Do the inference with a loaded model on specified features.
    
    Parameters
    ----------
    features : list[dict[str, str]]
        Feature to process.
        It a list of dict containing feature names as key and feature abstracted values as values.
    
    Returns
    -------
    A list of dict.
    All dict must have all three R, G, and B target. If one is missing, it will be considered as `null`.
    
    Notes
    -----
    The order must be kept for a response to be considered valid by the datacrunch arena.
    If more or less lines are returned, everything will be considered as invalid.
    Since it cannot check for line order mismatch, your results will still be considered as valid but will not be right.
    """
    
    # Loading received feature into a dataframe
    data = pandas.DataFrame(features)
    
    # Do prediction based on loaded model
    pred_r = model_r.predict(data)
    pred_g = model_g.predict(data)
    pred_b = model_b.predict(data)
    
    # Store result into a dataframe
    results = pandas.DataFrame({
        'r': pred_r,
        'g': pred_g,
        'b': pred_b
    })
    
    # Return result in a better format
    return list(results.T.to_dict().values())
