from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# --------------------
# App setup
# --------------------
app = FastAPI(title="Heart Disease Inference API")

# Load trained model
model = joblib.load("model.joblib")

# --------------------
# Request schema
# --------------------
class PredictionRequest(BaseModel):
    age: int
    gender: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# --------------------
# Root / health endpoint
# --------------------
@app.get("/")
def root():
    return {"status": "alive"}


# --------------------
# Prediction endpoint
# --------------------
@app.post("/predict")
def predict(request: PredictionRequest):
    df = pd.DataFrame([request.dict()])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][
        list(model.classes_).index("yes")
    ]

    return {
        "prediction": prediction,          # <-- string: "yes" / "no"
        "probability_yes": round(float(probability), 4)
    }
