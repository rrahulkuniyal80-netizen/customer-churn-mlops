from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline.prediction_pipeline import PredictionPipeline



class Customer(BaseModel):
    customerID: str
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


app = FastAPI()
pipeline = PredictionPipeline()

@app.get('/')

def home():
    return {"message": "Customer Churn Prediction API"}

@app.post("/predict")
def predict(customer: Customer):

    prediction = pipeline.predict(customer.model_dump())

    return {
        "prediction": "Churn" if prediction == 1 else "No Churn"
    }
