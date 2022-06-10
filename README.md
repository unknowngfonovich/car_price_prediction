# Project car price prediciton

## Usage

App can predict car price by entering some parameters.

## Installation and running

- (Docker running in progress)
- If you have conda - create environment from file `environment_create.yml`
- Activate environment and run command `uvicorn app.app:app --reload`

## Project structure

- `research` contains train and test datasets (folder `data`), jupyter notebook (file `processing_lesson.ipynb`) with EDA, data preparation, training models.
- `app` contains core files (folder `core` - ml models, pydantic schemas), main file - `app.py` 

## Model selection and score

The Ridge regression is used as model for car-price prediction. There are 2 models for type of cars: premium and regular.
The metric is MAE (mean absolute error) because data contains extremely high price. 
On test dataset MAE is ~1780. 
