from fastapi import FastAPI
from pydantic import BaseModel, validator
import pandas as pd
import joblib
import os
from pydantic.errors import PathNotExistsError
from sklearn.pipeline import Pipeline

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
            raise PathNotExistsError(f'Model with path `{path}` can not be found')

    def make_prediction(self, data: pd.DataFrame) -> float:

        
        """
        

        """
        
        return self.model.predict(data)

class Car(BaseModel):

    """
    Validation class for input Car with params

    :param model:           model of car, ex. Q7 or X5\n
    :type model:            str\n
    :param year:            year of car production, ex. 1970 or 2020 (max is 2020)\n
    :type year:             int\n
    :param transmission:    transmission type of car, ex. Auto\n
    :type transmission:     str\n
    :param mileage:         mileage of car ex. 3490.5 or 790231.2\n
    :type mileage:          float\n
    :param fuelType:        fueltype of car, ex. Hybrid or Petrol\n
    :type fuelType:         str\n
    :param tax:             ex. 300.2 or 20.0\n
    :type tax:              float\n
    :param engineSize:      ex.\n
    :type engineSize:       float\n
    :param car_maker:       ex.\n
    :type car_maker:        str
    """


    model:          str
    year:           int
    transmission:   str
    mileage:        float
    fuelType:       str
    tax:            float
    mpg:            float
    engineSize:     float
    car_maker:      str


    
    @validator('model')
    def check_model(cls, value):
        if ' ' in value:
            raise ValueError('Space found in model name, remove it!')
        elif value == '':
            raise ValueError('Model is empty!')
        return value

    @validator('year')
    def check_year_period(cls, value):
        low_b, up_b = 1970, 2020
        if value > up_b or value < low_b:
            raise ValueError(f'Year must be in interval ({low_b}, {up_b})')
        return value

    @validator('mileage')
    def check_neg_mileage(cls, value):
        if value < 0:
            raise ValueError('Mileage can not be negative!')
        return value

    @validator('tax')
    def check_neg_tax(cls, value):
        if value < 0:
            raise ValueError('Tax can not be negative!')
        return value

    @validator('engineSize')
    def check_neg_engsize(cls, value):
        if value < 0:
            raise ValueError('engineSize can not be negative!')
        return value

    @validator('car_maker')
    def check_maker(cls, value):
        if ' ' in value:
            raise ValueError('Space found in car_maker, remove it!')
        elif value == '':
            raise ValueError('Car_maker is empty!')
        return value

    @validator('transmission')
    def check_transmission(cls, value):
        if ' ' in value:
            raise ValueError('Space found in transmission, remove it!')
        elif value == '':
            raise ValueError('Transmission is empty!')
        return value

class Price(BaseModel):
    """
    Validation class for result of prediction
    
    """
    price:          float
    car:            dict

    @validator('price')
    def check_maker(cls, value):
        if value <= 0:
            raise ValueError('Price can not be negative!')
        return value


app = FastAPI()
premium_model, regular_model = PriceEstimator('models_ml/prem_model.pkl'), PriceEstimator('models_ml/reg_model.pkl')

@app.get('/')
def status_main():
    return {"message": "say hello"}

@app.post('/make_prediction', response_model=Price)
def make_predict(car: Car) -> Price:
    data = pd.DataFrame(data=car.dict(), index=[0])
    result = premium_model.make_prediction(data)[0] if car.car_maker.lower() in ('bmw', 'mercedes', 'audi') else regular_model.make_prediction(data)[0]
    return {
        'car': car.dict(),
        'price': result
        }

    

