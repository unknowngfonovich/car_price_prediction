# Project car price prediciton

## Usage

App can predict car price by entering some parameters.

## Installation

blabla
## Example running

## Project structure

- Folder `research` contains train and test datasets (folder `data`), jupyter notebook (file `processing_lesson.ipynb`) with EDA, data preparation, training models.

## Model selection and score

The Ridge regression is used as model for car-price prediction. There are 2 models for type of cars: premium and regular.
The metric is MAE (mean absolute error) because data contains extremely high price. 
On test dataset MAE is ~1780. 
