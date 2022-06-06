import joblib
import os
import pandas as pd

from sklearn.pipeline import Pipeline
from pydantic.errors import PathNotExistsError

class PriceEstimator:

    """

    Class for 

    :param path_to_model: path to file where model with extension .pkl is located
    :type: str

    """

    def __init__(self, path_to_model: str) -> None:
        self.model = self.load_model(path_to_model)
        self.path_model = path_to_model

    def load_model(self, path: str) -> Pipeline:

        """
        Method to load a model with extension .pkl by path

        :param path:    path to location of model
        :type path:     str

        """
        if os.path.isfile(path):
            return joblib.load(path)
        else:
            raise PathNotExistsError(path=path)

    def make_prediction(self, data: pd.DataFrame) -> float:

        
        """
        Method to make price prediction for car
        
        :param data: contains car info (model, year and etc.)
        :type data: pd.DataFrame
        """
        
        return self.model.predict(data)