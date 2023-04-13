import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras

# Load the saved models
models = {}
for product in ['Bread(400g)', 'Vegetable Oil (1L)','Milk (500ML)','Diesel (1L)','Maize meal (2kg)','Gasoline (1L)',
 'Inflation','Exchange Rate (USD)']:
    model = keras.models.load_model(f"{product}_time_series_model.h5")
    models[product] = model

# Define the forecast periods and dates
forecast_periods = 12
forecast_dates = pd.date_range(start='2023-04-01', periods=forecast_periods, freq='MS')

# Define the commodities, months, and years
commodities = ['Bread(400g)', 'Vegetable Oil (1L)','Milk (500ML)','Diesel (1L)','Maize meal (2kg)','Gasoline (1L)',
               'Inflation','Exchange Rate (USD)']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
years = [2023, 2024]

# Display the title of the app
st.title('PriceWise AI')

# Display the dropdowns for commodity, month and year selection
commodity = st.selectbox('Select Commodity', commodities)
month = st.selectbox('Select Month', months)
year = st.selectbox('Select Year', years)

# Load the data from the file
train_data = pd.read_csv("Time Series Data.csv")

n_steps= 3

# Create a dictionary to store the forecasted prices for each commodity
forecast_prices_dict = {}

# Get the last n_steps values from the training set
last_n_steps = train_data[commodity][-n_steps:].values.reshape(-1, 1)

# Create an empty list to store the forecasted prices
forecast_prices = []

# Loop through the forecast periods and make predictions
for i in range(forecast_periods):
    # Reshape the last_n_steps array for input into the model
    last_n_steps = last_n_steps.reshape(1, n_steps, 1)

    # Make a prediction using the model
    forecast = models[commodity].predict(last_n_steps)[0][0]

    # Append the forecast to the list of forecasted prices
    forecast_prices.append(forecast)

    # Update the last_n_steps array with the new forecasted value
    last_n_steps = np.vstack([last_n_steps[0][1:], [[forecast]]])

# Add the forecasted prices to the dictionary
forecast_prices_dict[commodity] = forecast_prices

# Display the forecasted prices for the selected commodity
st.write(f"\n{commodity} Forecasted Prices:")
for j in range(len(forecast_dates)):
    st.write(f"{forecast_dates[j].strftime('%B %Y')}: {forecast_prices_dict[commodity][j]:.2f}")