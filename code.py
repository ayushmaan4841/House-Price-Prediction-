# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Simulated dataset
data = {
    'area': [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000],
    'bedrooms': [3, 4, 3, 5, 4, 5, 4, 6, 5, 6],
    'bathrooms': [2, 3, 2, 4, 3, 4, 3, 4, 3, 5],
    'garage': [1, 2, 2, 3, 2, 3, 2, 3, 3, 4],
    'floors': [1, 2, 1, 2, 2, 2, 2, 3, 3, 3],
    'year_built': [2005, 2010, 2000, 2015, 2012, 2008, 2020, 2018, 2013, 2005],
    'location_score': [7, 8, 6, 9, 8, 9, 7, 9, 8, 9],  # Location score on a scale of 1-10
    'price': [300000, 400000, 350000, 500000, 450000, 600000, 550000, 700000, 650000, 800000]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Defining features and target
X = df[['area', 'bedrooms', 'bathrooms', 'garage', 'floors', 'year_built', 'location_score']]  # Features
y = df['price']  # Target

# Splitting the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Linear Regression model
model = LinearRegression()

# Training the model
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output the results
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
print("Predicted Prices:", y_pred)

# To predict on new data (area, bedrooms, bathrooms, garage, floors, year_built, location_score)
new_data = [[3200, 4, 3, 2, 2, 2017, 8]]  # Example new data
predicted_price = model.predict(new_data)
print("Predicted Price for new data:", predicted_price)
