import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('Car_Bazaar_System.db')

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/mikol/Desktop/Cars.csv')

# Write the data to a SQLite table
df.to_sql('Cars', conn, if_exists='append', index=False)

# Close the connection
conn.close()