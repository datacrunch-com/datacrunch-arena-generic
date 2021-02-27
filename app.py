import logging
import time
from typing import List, Dict

import fastapi
import inference
import pydantic

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class InferRequestModel(pydantic.BaseModel):
    """
    Model for infer requests.
    """
    
    features: List[Dict[str, float]]
    

# Create Fast API instance
app = fastapi.FastAPI()


# Define the /infer as a POST endpoint
@app.post("/infer")
async def infer(item: InferRequestModel):
    """
    API endpoint called with a POST request with the /infer URL.
    
    Parameters
    ----------
    item : InferRequestModel
        Request body.
        It will contain a list of `sub-requests`.
        This is to avoid doing multiple request when only one big is enough.
        We don't have much choice since Python is not made for multi-threading.
    
    Returns
    -------
    Prediction results.
    Since this will be a list of dict, it will automatically be converted to valid JSON.
    
    Notes
    -----
    The function call will log to the console the execution time.
    """
    
    # Store time before doing the computation
    start = time.perf_counter()
    
    # Do the inference
    results = inference.do(item.features)
    
    # Store time after the computation
    end = time.perf_counter()
    
    # Print how much time it took
    logger.debug("Execution time: {} seconds".format(end - start))
    
    return results


# Check if this file has been loaded from an import statement or directly with `python3 this_file.py`
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
