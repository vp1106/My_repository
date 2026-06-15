# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:15:08 2026

@author: Veda pramod
"""

#question 1

# # The Dataset
# X = [1, 2, 3, 4, 5, 6, 7, 8]
# Y = [50, 55, 65, 70, 75, 78, 85, 88]
# n = len(X)

# # 1. Calculate Averages (Means)
# mean_x = sum(X) / n
# mean_y = sum(Y) / n

# # 2. Calculate Slope (beta1)
# # We need the sum of (x - mean_x) * (y - mean_y) and (x - mean_x)^2
# numerator = 0
# denominator = 0

# for i in range(n):
#     numerator += (X[i] - mean_x) * (Y[i] - mean_y)
#     denominator += (X[i] - mean_x) ** 2

# beta1 = numerator / denominator

# # 3. Calculate Intercept (beta0)
# beta0 = mean_y - (beta1 * mean_x)

# # 4. Predict for 9 hours
# prediction_9 = beta0 + (beta1 * 9)

# # 5. Calculate Mean Squared Error (MSE)
# total_error = 0
# for i in range(n):
#     prediction = beta0 + (beta1 * X[i])
#     error = (Y[i] - prediction) ** 2
#     total_error += error

# mse = total_error / n



# print("Slope (beta1):", beta1)
# print("Intercept (beta0):", beta0)
# print("Predicted score for 9 hours:", prediction_9)
# print("Mean Squared Error (MSE):", mse)

# import matplotlib.pyplot as plt

# # 1. Create the scatter plot (the dots)
# plt.scatter(X, Y, color='blue', label='Actual Data')

# # 2. Create the regression line
# # We calculate the start and end points of the line using our beta0 and beta1
# line_y = []
# for x_value in X:
#     line_y.append(beta0 + (beta1 * x_value))

# plt.plot(X, line_y, color='red', label='Best Fit Line')

# # 3. Add labels and show it
# plt.xlabel('Hours Studied')
# plt.ylabel('Exam Score')
# plt.title('Study Hours vs Score')
# plt.legend()
# plt.show()


# #question 2

# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

# # 1. Define the input matrix X (Features) and output Y (Price)
# # Each sub-list is [Size, Bedrooms, Age]
# X = [
#     [800, 2, 20],
#     [1000, 2, 15],
#     [1200, 3, 10],
#     [1500, 3, 8],
#     [1800, 4, 5],
#     [2000, 4, 3],
#     [2200, 5, 2],
#     [2500, 5, 1]
# ]

# Y = [40, 50, 65, 75, 90, 105, 120, 135]

# # 2. Fit the Model
# model = LinearRegression()
# model.fit(X, Y)

# # 3. Compute Coefficients
# # beta0 is the intercept, the others are for Size, Bedrooms, and Age
# beta0 = model.intercept_
# coefficients = model.coef_

# print("--- Model Parameters ---")
# print("Intercept (beta0):", beta0)
# print("Coefficient for Size (beta1):", coefficients[0])
# print("Coefficient for Bedrooms (beta2):", coefficients[1])
# print("Coefficient for Age (beta3):", coefficients[2])
# print("")

# # 4. Predict price for a new house
# # Example: 1600 sq.ft, 3 bedrooms, 10 years old
# new_house = [[1600, 3, 10]]
# predicted_price = model.predict(new_house)

# print("--- Prediction ---")
# print("Predicted Price for 1600sqft, 3BR, 10yrs:", predicted_price[0], "Lakhs")
# print("")

# # 5. Evaluate using MSE
# all_predictions = model.predict(X)
# mse = mean_squared_error(Y, all_predictions)

# print("--- Evaluation ---")
# print("Mean Squared Error (MSE):", mse

# question 3


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('ice_cream_sales_vs_temperature.csv')
X = df['Temperature_C'].values
Y = df['Ice_Cream_Sales'].values
n = len(X)

# 2. Hyperparameters
learning_rate = 0.001  # How big of a step to take
epochs = 1000          # How many times to repeat the process

# Initial guesses for coefficients
beta1 = 0.0
beta0 = 0.0

# Lists to store history for plotting the cost function
cost_history = []

# 3. Gradient Descent Loop
for i in range(epochs):
    # Calculate predictions (Y = b0 + b1*X)
    predictions = beta0 + (beta1 * X)
    
    # Calculate the error (Cost)
    error = predictions - Y
    cost = (1 / (2 * n)) * np.sum(error**2)
    cost_history.append(cost)
    
    # Calculate Gradients (the direction to move)
    # Derivative of cost with respect to beta0 and beta1
    d_beta0 = (1 / n) * np.sum(error)
    d_beta1 = (1 / n) * np.sum(error * X)
    
    # Update coefficients
    beta0 = beta0 - (learning_rate * d_beta0)
    beta1 = beta1 - (learning_rate * d_beta1)

# --- Results ---
print(f"Final Slope (beta1): {beta1}")
print(f"Final Intercept (beta0): {beta0}")
print(f"Final Cost: {cost_history[-1]}")

# 4. Plotting
plt.figure(figsize=(12, 5))

# Plot 1: The Best-Fit Line
plt.subplot(1, 2, 1)
plt.scatter(X, Y, color='blue', alpha=0.5, label='Actual Data')
plt.plot(X, beta0 + beta1 * X, color='red', label='GD Fit Line')
plt.title('Ice Cream Sales vs Temp')
plt.xlabel('Temperature (°C)')
plt.ylabel('Sales')
plt.legend()

# Plot 2: The Cost Function (should go down over time)
plt.subplot(1, 2, 2)
plt.plot(range(epochs), cost_history, color='green')
plt.title('Cost Function over Time')
plt.xlabel('Epochs')
plt.ylabel('MSE Cost')

plt.tight_layout()
plt.show()