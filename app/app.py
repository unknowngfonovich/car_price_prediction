from fastapi import FastAPI
from app.core.schemas.schema import Price, Car
from app.core.ml.estimator.car_estimator import (
    pd,
    PriceEstimator
)


app = FastAPI()
premium_model, regular_model = PriceEstimator('app/core/ml/models_storage/prem_model.pkl'), PriceEstimator('app/core/ml/models_storage/reg_model.pkl')

@app.get('/')
def status_main():
    return {"message": "say hello"}

@app.post('/make_prediction', response_model=Price)
def make_predict(car: Car) -> Price:
    data = pd.DataFrame(data=car.dict(), index=[0])
    result = premium_model.make_prediction(data)[0] if car.car_maker.lower() in ('bmw', 'mercedes', 'audi') else regular_model.make_prediction(data)[0]
    return {
        'car': car.dict(),
        'price': round(result, 2)
        }

    

