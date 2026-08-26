import streamlit as st
import requests

# Fast API endpint URL
API_URL = "http://127.0.0.1:8000/predict_api"

# Page configuration
st.set_page_config(
    page_title="California Housing Price Prediction",
    page_icon="🏠",

)

st.title("California Housing Price Prediction")
st.write("Enter the house house information below to preidict the price of the house in California.")

# Input fields for user to enter house information
MedInc = st.number_input("Median Income (in $10,000s)",min_value=0.0,step=0.1,value=3.0)
HouseAge = st.number_input("House Age (in years)",min_value=0.0,step=1.0,value=20.0)
AveRooms = st.number_input("Average Number of Rooms per Household",min_value=0.0,step=0.1,value=5.0)
AveBedrms = st.number_input("Average Number of Bedrooms per Household",min_value=0.0,step=0.1,value=1.0)
Population = st.number_input("Population of the Area",min_value=0.0,step=1.0,value=1000.0)
AveOccup = st.number_input("Average Occupancy per Household",min_value=0.0,step=0.1,value=3.0)
Latitude = st.number_input("Latitude",min_value=-90.0,max_value=90.0,step=0.1,value=35.0)
Longitude = st.number_input("Longitude",min_value=-180.0,max_value=180.0,step=0.1,value=-119.0)

# Prediction button
if st.button("Predict House Price"):
    # Data to send to FastApi
    data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }

    try:
        # Send Post request to FastAPI endpoint
        response = requests.post(API_URL, json=data)
        response.raise_for_status() # Raise an error for bad responses

        # Check response
        if response.status_code == 200:
            result = response.json()
            predicted_price = result["predicted_price"]

            st.success(f"Predicted House Price: ${predicted_price:,.2f}")

        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(
                f"Could not connect to FastAPI. "
                f"Make sure the FastAPI server is running. Error: {e}"
        )
