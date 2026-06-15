# 17 th APRIL LAB
# import pandas as pd
# import numpy as np

# # 1. LOAD DATA
# # Ensure the filename matches your actual file
# df = pd.read_csv('weather_forecast_data.csv')

# # 2. PREPROCESSING
# # Fill missing numbers with the average
# df = df.fillna(df.mean(numeric_only=True))

# # IMPORTANT: Mapping the exact words used in the Zeeshier dataset
# # The dataset uses 'rain' and 'no rain'
# df['Rain'] = df['Rain'].str.lower().map({'rain': 1, 'no rain': 0})

# # Drop rows if mapping failed (just in case of weird formatting)
# df = df.dropna(subset=['Rain'])

# # Select features (X) and target (y)
# y = df['Rain'].values.reshape(-1, 1)
# X_raw = df.drop(['Rain'], axis=1)

# # Handle text columns and convert to numbers
# X_raw = pd.get_dummies(X_raw)

# # Normalization (Crucial for Gradient Descent to work!)
# X_scaled = (X_raw - X_raw.min()) / (X_raw.max() - X_raw.min())
# X = X_scaled.values

# # Add a column of 1s for the 'bias'
# X = np.c_[np.ones(X.shape[0]), X]

# # 3. TRAIN/TEST SPLIT (80% train, 20% test)
# split = int(0.8 * len(X))
# X_train, X_test = X[:split], X[split:]
# y_train, y_test = y[:split], y[split:]

# # 4. LOGISTIC REGRESSION MATH
# def sigmoid(z):
#     return 1 / (1 + np.exp(-z.astype(float)))

# weights = np.zeros((X_train.shape[1], 1))
# learning_rate = 0.5  # Increased slightly to help it learn faster
# iterations = 3000

# for i in range(iterations):
#     z = np.dot(X_train, weights)
#     predictions = sigmoid(z)
#     error = predictions - y_train
#     gradient = np.dot(X_train.T, error) / len(y_train)
#     weights -= learning_rate * gradient

# # 5. EVALUATE ON TEST DATA
# test_z = np.dot(X_test, weights)
# test_probs = sigmoid(test_z)


# # Threshold: If prob > 0.5, it's 1 (Rain), otherwise 0
# final_preds = (test_probs >= 0.5).astype(int)

# # Use your requested formulas
# TP = np.sum((final_preds == 1) & (y_test == 1))
# TN = np.sum((final_preds == 0) & (y_test == 0))
# FP = np.sum((final_preds == 1) & (y_test == 0))
# FN = np.sum((final_preds == 0) & (y_test == 1))

# # Prevent division by zero with small 'epsilon' or if checks
# accuracy  = (TP + TN) / len(y_test)
# precision = TP / (TP + FP) if (TP + FP) > 0 else 0
# recall    = TP / (TP + FN) if (TP + FN) > 0 else 0
# f1_score  = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# print("--- Final Results ---")
# print(f"Accuracy:  {accuracy:.2%}")
# print(f"Precision: {precision:.4f}")
# print(f"Recall:    {recall:.4f}")
# print(f"F1-Score:  {f1_score:.4f}")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def generate_geometry_data(samples_per_shape=100):
    data = []
    labels = []

    for _ in range(samples_per_shape):
        # 1. CIRCLE (Label 0)
        r = np.random.uniform(5, 20)
        area = np.pi * (r**2)
        perim = 2 * np.pi * r
        circ = (4 * np.pi * area) / (perim**2) # Will be exactly 1.0
        data.append([area, circ])
        labels.append(0)

        # 2. RECTANGLE (Label 1)
        w = np.random.uniform(10, 30)
        h = np.random.uniform(10, 30)
        area = w * h
        perim = 2 * (w + h)
        circ = (4 * np.pi * area) / (perim**2) # Usually around 0.7-0.8
        data.append([area, circ])
        labels.append(1)

        # 3. TRIANGLE (Label 2)
        base = np.random.uniform(10, 30)
        height = np.random.uniform(10, 30)
        area = 0.5 * base * height
        # Simplified perimeter for an isosceles triangle
        side = np.sqrt((base/2)**2 + height**2)
        perim = base + (2 * side)
        circ = (4 * np.pi * area) / (perim**2) # Usually around 0.5-0.6
        data.append([area, circ])
        labels.append(2)

    return np.array(data), np.array(labels)

# --- EXECUTION ---

# 1. Create Data
X, y = generate_geometry_data(200)

# 2. Normalize (Standardize)
# This is crucial because Area (~1200) and Circularity (~1.0) have different scales
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 4. Train SVM Models with different kernels
kernels = ['linear', 'poly', 'rbf']
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for i, kernel_type in enumerate(kernels):
    # Train
    model = svm.SVC(kernel=kernel_type, C=1.0)
    model.fit(X_train, y_train)
    
    # Plotting Decision Boundaries
    h = .02
    x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
    y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    axes[i].contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
    axes[i].scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, edgecolors='k', cmap='viridis', s=20)
    axes[i].set_title(f"SVM with {kernel_type} kernel\nAcc: {model.score(X_test, y_test):.2%}")
    axes[i].set_xlabel("Scaled Area")
    axes[i].set_ylabel("Scaled Circularity")

plt.show()