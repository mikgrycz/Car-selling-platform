# Import necessary libraries
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf
from tensorflow import keras
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
import category_encoders as ce
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error
import os
# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the CSV file
csv_file = os.path.join(current_dir, 'car_listings.csv')

# Read the CSV file
data = pd.read_csv(csv_file)

# Print the column names and the shape of the data
print(data.columns)
print(data.shape)

# Filter out rows where 'engine_volume' or 'fuel_type' is 'Elektryczny'
data = data[data['engine_volume'] != 'Elektryczny']
data = data[data['fuel_type'] != 'Elektryczny']

# Drop rows with less than 13 non-NA values
data = data.dropna(thresh=13)

# Remove duplicate records by 'ID'
data = data.drop_duplicates(subset='ID')

# Print rows with any NA values
nan_rows = data[data.isna().any(axis=1)]
print(f"nan rows={nan_rows}")

# Drop the 'fuel_type' column
data = data.drop('fuel_type', axis=1)

# Encode categorical features
encoders = {}
for col in ['brand', 'model', 'transmission', 'bodytype', 'colour']:
    le = LabelEncoder()
    le.fit(data[col])
    data[col] = le.transform(data[col])
    encoders[col] = le  # Store the fitted encoder for future use

# Print the classes for 'brand' and 'model' encoders
print(encoders['brand'].classes_)
print(encoders['model'].classes_)
# Drop rows where all columns are NaN
data = data.dropna(how='all')

# Save the encoders for future use
joblib.dump(encoders, 'encoders.pkl')

# Print unique values in the 'currency' column
print(data['currency'].unique())

# Remove spaces from 'price' and 'ID' columns
data['price'] = data['price'].str.replace(' ', '')
data['ID'] = data['ID'].str.replace('ID: ', '')

# Drop the 'ID' column
data = data.drop('ID', axis=1)

# Remove spaces and 'km' from 'mileage' column
data['mileage'] = data['mileage'].str.replace(' ', '')
data['mileage'] = data['mileage'].str.replace('km', '')

# Remove spaces and 'cm3' from 'engine_volume' column
data['engine_volume'] = data['engine_volume'].str.replace(' ', '')
data['engine_volume'] = data['engine_volume'].str.replace('cm3', '')

# Remove spaces and 'KM' from 'power' column
data['power'] = data['power'].str.replace(' ', '')
data['power'] = data['power'].str.replace('KM', '')

# List of columns to clean
cols = ['price', 'year', 'mileage', 'engine_volume', 'power']

# Clean the columns
for col in cols:
    # Convert column to string
    data[col] = data[col].astype(str)
    # Remove non-numeric characters
    data[col] = data[col].str.replace(r'\D', '')
    # Convert column to numeric, non-numeric become NaN
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Drop rows with NaN values in the specified columns
data = data.dropna(subset=cols)

# Convert 'power' and 'price' columns to numeric
data['power'] = pd.to_numeric(data['power'], errors='coerce')
data['price'] = pd.to_numeric(data['price'], errors='coerce')

# Drop rows with NaN values in 'power' column
data = data.dropna(subset=['power'])

# Conversion rates for different currencies to PLN
conversion_rates = {'EUR': 4.5, 'USD': 3.8, 'GBP': 5.2}

# Convert 'price' to PLN based on 'currency' column
for currency, rate in conversion_rates.items():
    data['price'] = np.where(data['currency'] == currency, data['price'] * rate, data['price'])

# Drop the 'currency' column
data = data.drop('currency', axis=1)

# Reset the index of the DataFrame
data.reset_index(drop=True, inplace=True)

# Print the DataFrame and its columns for debugging
print(data)
print(data.columns)

# Print the shape of the DataFrame
print(f' data shape: {data.shape}')

# Separate the target variable 'price' from the features
y = data['price']
data = data.drop('price', axis=1)
x = data

# Print the shapes of the features and target variable
print(x.shape)
print(y.shape)

# Standardize the features using StandardScaler
scaler = StandardScaler()
x = scaler.fit_transform(x)

# Save the scaler for future use
joblib.dump(scaler, 'scaler.pkl')

# Print the shape of the DataFrame
print(f' data shape: {data.shape}')

# Print the shapes of the features and target variable
print("SHAPE")
print(x.shape)
print(y.shape)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Print the shapes of the training and testing sets
print(f'x_train shape: {x_train.shape}, x_test shape: {x_test.shape}, y_train shape: {y_train.shape}, y_test shape: {y_test.shape}')

# Train a linear regression model
model_1 = linear_model.LinearRegression()
model_1.fit(x_train, y_train)

# Make predictions on the training and testing sets
pred_train = model_1.predict(x_train)
pred_test = model_1.predict(x_test)

# Print the RMSE of the model on the training and testing sets
model_2 = keras.Sequential([Dense(80, input_shape=[9], activation='softmax'),
                           Dense(70, activation='relu'),
                           Dense(60, activation='relu'),
                           Dense(50, activation='relu'),
                           Dense(40, activation='relu'),
                           Dense(30, activation='relu'),
                           Dense(10, activation='relu'),
                           Dense(1)])

model_3 = keras.Sequential([Dense(20, input_shape=[9], activation='relu'),
                           Dense(40, activation='sigmoid'),
                           Dense(10, activation='relu'),
                           Dense(1)])

model_4 = keras.Sequential([Dense(7, input_shape=[9], activation='relu'),
                            Dense(6, activation='softmax'),
                            Dense(5, activation='relu'),
                            Dense(1)])
models = [model_2, model_3, model_4]#
names = ['model_2', 'model_3', 'model_4']#
results = []
# Print a message indicating the start of model training
print("training models: ")

# Loop over each model in the list of models
for i, model in enumerate(models):
    # Compile the model with the Adam optimizer and mean squared error loss function
    model.compile(optimizer='adam', loss='mean_squared_error',metrics=['mean_absolute_error'])

    # Fit the model to the training data
    model.fit(x_train, y_train, epochs=500, batch_size=1000)

    # Use the trained model to make predictions on the training and testing data
    pred_train = model.predict(x_train)
    pred_test = model.predict(x_test)

    # Append the model's performance metrics to the results list
    results.append(f'MAE on train: {mean_absolute_error(y_train, pred_train)},  MAE on test: {mean_absolute_error(y_test, pred_test)}')

    # Save the trained model to a file
    model.save(f'{names[i]}.keras')

# Print a separator for readability
print(f'##################################')

# Loop over each result in the results list
print(f'Linear regression MSE on train: {mean_absolute_error(y_train, pred_train)}, MSE on test: {mean_absolute_error(y_test, pred_test)}')
for result in results:
    # Print the result
    print(result)

    # Print a separator for readability
    print(f'##################################')

