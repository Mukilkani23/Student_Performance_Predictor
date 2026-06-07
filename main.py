from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Load the saved model once when server starts
model = joblib.load("student_model.pkl")

# Create the FastAPI app
app = FastAPI()

# Define what input data looks like
# Pydantic validates that all fields are present and correct type
class StudentData(BaseModel):
    G1: float
    G2: float
    age: float
    studytime: float
    failures: float
    absences: float
    famrel: float
    freetime: float
    goout: float
    Dalc: float
    Walc: float
    health: float

# Root route — just to confirm server is running
@app.get("/")
def home():
    return {"message": "Student Performance Predictor API is running"}

@app.get("/app")
def serve_frontend():
    return FileResponse("index.html")

# Prediction route — this is where the magic happens
@app.post("/predict")
def predict(data: StudentData):
    # Convert incoming data to numpy array (what model expects)
    input_array = np.array([[
        data.G1, data.G2, data.age, data.studytime,
        data.failures, data.absences, data.famrel,
        data.freetime, data.goout, data.Dalc,
        data.Walc, data.health
    ]])
    
    # Run prediction
    prediction = model.predict(input_array)
    predicted_grade = round(float(prediction[0]), 2)
    
    return {
        "predicted_G3": predicted_grade,
        "message": f"Predicted final grade is {predicted_grade} out of 20"
    }