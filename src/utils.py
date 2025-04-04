import os
import sys
import numpy as np
import pandas as pd

from src.exception import CustomException

import dill

def save_object(obj, file_path):
    """
    Save the object to a file using pickle.
    Args:
        obj: The object to be saved.
        file_path: The path where the object will be saved.
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)