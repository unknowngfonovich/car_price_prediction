# Project car price prediciton

## Usage

App can predict car price by entering some parameters.

## Installation and running

- (Docker running in progress)
- If you have conda - create environment from file `environment_create.yml`
- Activate environment and run command `uvicorn app.app:app --reload`

    If you have Postman try to make POST request to `http://127.0.0.1:8000/make_prediction` with body:
    { 
        "model": "Q7",
        "year": 2020,
        "transmission": "Auto",
        "mileage": 30.0,
        "fuelType": "Petrol",
        "tax": 20.0,
        "mpg": 87.0,
        "engineSize": 4.0,
        "car_maker": "Audi"
    }
    
    You will recieve JSON with price and body of request.

## Project structure

- `research` contains train and test datasets (folder `data`), jupyter notebook (file `processing_lesson.ipynb`) with EDA, data preparation, training models.
- `app` contains core files (folder `core` - ml models, pydantic schemas), main file - `app.py` 

## Model selection and score

The Ridge regression is used as model for car-price prediction. There are 2 models for type of cars: premium and regular.
The metric is MAE (mean absolute error) because data contains extremely high price. 
On test dataset MAE is ~1780. 
