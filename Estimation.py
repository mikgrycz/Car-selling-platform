import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
import os
def predict_car_price(features):
    # Load the model
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model = load_model(os.path.join(dir_path, 'model_2.keras'))

    # Load the encoders and scaler
    encoders = joblib.load(os.path.join(dir_path, 'encoders.pkl'))
    scaler = joblib.load(os.path.join(dir_path, 'scaler.pkl'))

    for col in ['brand', 'model', 'transmission', 'bodytype', 'colour']:
        features[col] = encoders[col].transform(features[col])

    cols = ['year', 'mileage', 'engine_volume', 'power']
    for col in cols:
        # Convert column to string
        features[col] = features[col].astype(str)
        # Remove non-numeric characters
        features[col] = features[col].str.replace(r'\D', '')
        # Convert column to numeric, non-numeric become NaN
        features[col] = pd.to_numeric(features[col], errors='coerce')

    features = scaler.transform(features)

    # Make a prediction
    prediction = model.predict(features)

    return prediction

# Test the function
features = pd.DataFrame([['Ford', 'Mustang', 2019, '123971', '5038', 450, 'Automatyczna', 'Kabriolet', 'Biały']],
                        columns=['brand', 'model', 'year', 'mileage', 'engine_volume', 'power', 'transmission', 'bodytype', 'colour'])
print(predict_car_price(features))