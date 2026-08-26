import pickle
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel

# create FastAPI instance
app = FastAPI()

# Load trained model  and scaler
regmodel = pickle.load(open("regmodel.pkl", "rb"))
scaler = pickle.load(open("scaling.pkl", "rb"))

# Input features for prediction
class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to the California Housing Price Prediction API!"}

@app.post("/predict_api")
def predict_api(data: HouseData):
    # Convert input data to DataFrame
    input_data = pd.DataFrame([data.dict()])

    # input_data = np.array([
    #     data["MedInc"],
    #     data["HouseAge"],
    #     data["AveRooms"],
    #     data["AveBedrms"],
    #     data["Population"],
    #     data["AveOccup"],
    #     data["Latitude"],
    #     data["longitude"]
    # ]).reshape(1, -1)

    print("Inpput data:", input_data)

    # Scale the input data
    scaled_data = scaler.transform(input_data)

    print("Scaled data:", scaled_data)

    # Make prediction
    prediction = regmodel.predict(scaled_data)
    print(f"Prediction: {prediction[0]}")

    return {
        "predicted_price": prediction[0]
    }



