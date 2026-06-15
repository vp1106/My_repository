# KMEANS CLUSTERING
"""
Created on Sat Apr 25 12:36:33 2026

@author: Veda pramod
"""

# import numpy as np
# import matplotlib.pyplot as plt

# # 1. Dataset Initialization
# X = np.array([
#     [1.0, 2.0], [1.5, 1.8], [5.0, 8.0], 
#     [8.0, 8.0], [1.0, 0.6], [9.0, 11.0], 
#     [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
# ])

# def run_kmeans(data, k, initial_indices):
#     # 2. Manual Centroid Initialization
#     centroids = data[initial_indices]
    
#     # Perform 2 iterations
#     for i in range(2):
#         # 4. Assign clusters (Euclidean distance)
#         distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
#         labels = np.argmin(distances, axis=1)
        
#         # 5. Update centroids
#         new_centroids = np.array([data[labels == j].mean(axis=0) for j in range(k)])
#         centroids = new_centroids
    
#     return labels, centroids

# # Apply K=2 (Initial centroids: P1 and P6)
# labels_k2, final_c_k2 = run_kmeans(X, k=2, initial_indices=[0, 5])

# # Apply K=3 (Initial centroids: P1, P3, and P8)
# labels_k3, final_c_k3 = run_kmeans(X, k=3, initial_indices=[0, 2, 7])

# # 6. Plotting
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# # Plot K=2
# ax1.scatter(X[:, 0], X[:, 1], c=labels_k2, cmap='viridis', s=100)
# ax1.scatter(final_c_k2[:, 0], final_c_k2[:, 1], c='red', marker='X', s=200, label='Centroids')
# ax1.set_title("K-Means (k=2) after 2 Iterations")
# ax1.grid(True); ax1.legend()

# # Plot K=3
# ax2.scatter(X[:, 0], X[:, 1], c=labels_k3, cmap='Set1', s=100)
# ax2.scatter(final_c_k3[:, 0], final_c_k3[:, 1], c='black', marker='X', s=200, label='Centroids')
# ax2.set_title("K-Means (k=3) after 2 Iterations")
# ax2.grid(True); ax2.legend()

# plt.show()



# PCA PRINCIPAL COMPONENT ANALYSIS

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # 1. Dataset Setup
# data = {
#     'F1': [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1],
#     'F2': [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9],
#     'F3': [1.2, 0.3, 1.5, 1.3, 1.8, 1.6, 1.0, 0.6, 0.8, 0.5],
#     'F4': [0.5, 0.2, 0.7, 0.6, 0.9, 0.8, 0.4, 0.3, 0.4, 0.2]
# }
# df = pd.DataFrame(data)

# # --- PCA Pipeline ---

# # Step 1: Standardization (Zero mean, Unit variance)
# df_std = (df - df.mean()) / df.std()

# # Step 2: Compute Covariance Matrix
# cov_matrix = df_std.cov()

# # Step 3 & 4: Eigen-decomposition and Sorting
# eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
# idx = eigenvalues.argsort()[::-1] # Get indices for descending sort
# eigenvalues = eigenvalues[idx]
# eigenvectors = eigenvectors[:, idx]

# # Step 5: Select top k=2 components
# W = eigenvectors[:, :2]

# # Step 6: Project data onto new 2D space
# X_pca = df_std.values.dot(W)

# # Step 7: Visualize
# plt.figure(figsize=(8, 5))
# plt.scatter(X_pca[:, 0], X_pca[:, 1], c='teal', s=100, edgecolors='k')
# plt.title("PCA Projection (4D -> 2D)")
# plt.xlabel(f"PC1 ({eigenvalues[0]/sum(eigenvalues)*100:.1f}% Variance)")
# plt.ylabel(f"PC2 ({eigenvalues[1]/sum(eigenvalues)*100:.1f}% Variance)")
# plt.grid(alpha=0.3)
# plt.show()

import numpy as np
from sklearn.neighbors import NearestNeighbors

# 1. Load data
data = np.loadtxt('armadillo.xyz')
points = data[:, :3]      # First 3 columns: x, y, z
gt_normals = data[:, 3:]  # Last 3 columns: nx, ny, nz

def estimate_normals_pca(points, k=10):
    n_points = points.shape[0]
    normals = np.zeros((n_points, 3)) # This is shape (N, 3)
    
    nbrs = NearestNeighbors(n_neighbors=k).fit(points)
    _, indices = nbrs.kneighbors(points)
    
    for i in range(n_points):
        # Slice only the coordinates for the neighborhood
        neighborhood = points[indices[i]] 
        
        # PCA steps
        centered = neighborhood - np.mean(neighborhood, axis=0)
        cov = np.dot(centered.T, centered) / k
        
        # eigenvectors will now be 3x3 because cov is 3x3
        eigenvalues, eigenvectors = np.linalg.eigh(cov)
        
        # eigenvectors[:, 0] is now shape (3,), matching normals[i]
        normals[i] = eigenvectors[:, 0]
        
    return normals

# 2. Run estimation
k_val = 10
pred_normals = estimate_normals_pca(points, k=k_val)

# 3. Compute Angular Error (as per your requirement)
# Normalize both to be safe
pred_normals /= np.linalg.norm(pred_normals, axis=1, keepdims=True)
gt_normals /= np.linalg.norm(gt_normals, axis=1, keepdims=True)

# Compute error: arccos(abs(dot product))
dot_products = np.abs(np.sum(pred_normals * gt_normals, axis=1))
dot_products = np.clip(dot_products, -1.0, 1.0)
errors = np.degrees(np.arccos(dot_products))

print(f"Mean Angular Error for k={k_val}: {np.mean(errors):.2f} degrees")