#Read userts input and then Convert users input from the terminal to the DataFrame
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
import os
from Estimation import predict_car_price

def get_input():
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    year = input("Enter the year: ")
    mileage = input("Enter the mileage: ")
    engine_volume = input("Enter the engine volume: ")
    power = input("Enter the power: ")
    transmission = input("Enter the transmission: ")
    bodytype = input("Enter the bodytype: ")
    colour = input("Enter the colour: ")

    features = pd.DataFrame([[brand, model, year, mileage, engine_volume, power, transmission, bodytype, colour]],
                            columns=['brand', 'model', 'year', 'mileage', 'engine_volume', 'power', 'transmission', 'bodytype', 'colour'])
    result =  predict_car_price(features)
    print(result)
    return result
get_input()
