import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
import category_encoders as ce
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error
# labels:   ["Marka pojazdu", "Model pojazdu", "Rok produkcji", "Przebieg", "Pojemność skokowa", "Rodzaj paliwa", "Moc", "Skrzynia biegów", "Napęd", "Typ nadwozia", "Liczba drzwi", "Liczba miejsc", "Kolor"]
# # check gpus available
# print(tf.config.experimental.list_physical_devices('GPU'))
# naped i liczba drzwi/miejsc
data = pd.read_csv("car_listings.csv")
print(data.columns)
print(data.shape)
data = data[data['engine_volume'] != 'Elektryczny']
data = data[data['fuel_type'] != 'Elektryczny']
data = data.dropna(thresh=13)
data = data.drop_duplicates(subset='ID')
nan_rows = data[data.isna().any(axis=1)]
data = data.drop('fuel_type', axis=1)

print(f"nan rows={nan_rows}")

# remove duplicate records by ID

# drop empty rows
le = LabelEncoder()
for col in ['brand', 'model', 'transmission', 'bodytype', 'colour']:
    le.fit(data[col])
    data[col] = le.transform(data[col])
data = data.dropna(how='all')

# there is a column price and column currency, we need to convert the price to a single currency PLN
print(data['currency'].unique())
data['price'] = data['price'].str.replace(' ', '')
data['ID'] = data['ID'].str.replace('ID: ', '')
data = data.drop('ID', axis=1)
data['mileage'] = data['mileage'].str.replace(' ', '')
data['mileage'] = data['mileage'].str.replace('km', '')
data['engine_volume'] = data['engine_volume'].str.replace(' ', '')
data['engine_volume'] = data['engine_volume'].str.replace('cm3', '')
data['power'] = data['power'].str.replace(' ', '')
data['power'] = data['power'].str.replace('KM', '')
cols = ['price', 'year', 'mileage', 'engine_volume', 'power']
for col in cols:
    # Convert column to string
    data[col] = data[col].astype(str)
    # Remove non-numeric characters
    data[col] = data[col].str.replace(r'\D', '')
    # Convert column to numeric, non-numeric become NaN
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Drop rows with NaN values in the specified columns
data = data.dropna(subset=cols)


data['power'] = pd.to_numeric(data['power'], errors='coerce')
data = data.dropna(subset=['power'])
data['price'] = pd.to_numeric(data['price'], errors='coerce')




conversion_rates = {'EUR': 4.5, 'USD': 3.8, 'GBP': 5.2}
for currency, rate in conversion_rates.items():
    data['price'] = np.where(data['currency'] == currency, data['price'] * rate, data['price'])
data = data.drop('currency', axis=1)

#data = pd.DataFrame(data)
data.reset_index(drop=True, inplace=True)


print(data)
print(data.columns)
print("###################@#@@###")
#data = data.isna().sum()
print(f' data shape: {data.shape}')
y = data['price']
data = data.drop('price', axis=1)
x = data
print(x.shape)
print(y.shape)
print("1111111")
scaler = StandardScaler()
x = scaler.fit_transform(x)

#data = pd.DataFrame(data)

#print(data.columns)

print(f' data shape: {data.shape}')

print("SHAPE")
print(x.shape)
print(y.shape)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print(f'x_train shape: {x_train.shape}, x_test shape: {x_test.shape}, y_train shape: {y_train.shape}, y_test shape: {y_test.shape}')

model_1 = linear_model.LinearRegression()
model_1.fit(x_train, y_train)
pred_train = model_1.predict(x_train)
pred_test = model_1.predict(x_test)
print(f'Linear regression RMSE on train: {mean_squared_error(y_train, pred_train, squared=False)}, RMSE on test: {mean_squared_error(y_test, pred_test, squared=False)}')


model_2 = keras.Sequential([Dense(30, input_shape=[9], activation='softmax'),
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
models = [model_2, model_3, model_4]
names = ['model_2', 'model_3', 'model_4']
results = []
print("training models: ")
for i, model in enumerate(models):
    model.compile(optimizer='adam', loss='mean_squared_error',metrics=['mean_absolute_error'])

    model.fit(x_train, y_train, epochs=1000, batch_size=300)
    pred_train = model.predict(x_train)
    pred_test = model.predict(x_test)
    #results.append(f'{model} RMSE on train: {mean_squared_error(y_test, pred_test, squared=False)},{model} RMSE on test: {mean_squared_error(y_train, pred_train, squared=False)}, accuracy {model.evaluate(x_test, y_test)}')
    results.append(f'MAE on train: {mean_absolute_error(y_train, pred_train)},  MAE on test: {mean_absolute_error(y_test, pred_test)}, model evaluation: {model.evaluate(x_test, y_test)}')
    model.save(f'{names[i]}.h5')
    
print(f'##################################')
for result in results:
    print(result)
    print(f'##################################')
i = 0
# while i < len(models):
#     models[i].save(f'{names[i]}.h5')
