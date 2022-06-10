from pydantic import BaseModel, validator

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
    :type car_maker:        str\n


    There are validators for each car parameter (check if value is negative or not,\n
    check if value is outer of bound
    )

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