# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:11:23 2026

@author: Veda pramod
"""

#bracketing method

# def J(w):
#     return (w^2 + (54/w))

# def first_derivative(f, x, h=1e-5):
#     return (f(x + h) - f(x)) / h
    
   
def J(w):
    return w**2 + (54/w) #function definition

def bracketing_method(w_start, step):
    """Finds an interval [a, b] containing the minimum."""
    w1 = w_start #specified by the user
    w2 = w1 + step #incremented value
    
    # Ensure we are moving in the descending direction
    if J(w2) > J(w1): #if the second value is higher than first-we are moving in opp direction to minimum-switch the step
        step = -step #change sign if min  lies in the opposite direction
        w2 = w1 + step
        
    while J(w2) < J(w1): #while loop for iteration until you reach minimum 
    #loop until the previous point is lesser than the current point 
    #when loop ends J(w2)>J(w1)
        w1 = w2
        w2 = w1 + step
        
    # Sort to return [lower, upper]
    return sorted([w1 - step, w2])

def interval_halving(a, b, epsilon=0.01, iterations=15):#any way to find no of iteration without trial and error
    """Narrows down the bracket to find the critical point."""
    for i in range(iterations):
        mid = (a + b) / 2
        w1 = mid - (epsilon / 2)
        w2 = mid + (epsilon / 2)
        
        if J(w1) < J(w2):
            b = w2
        else:
            a = w1
            
    return (a + b) / 2

# --- Execution ---
# 1. Bracket the function starting at w=1
bracket = bracketing_method(w_start=1, step=1)
print(f"Bracketed Interval: {bracket}")

# 2. Find critical point within that bracket
critical_point = interval_halving(bracket[0], bracket[1])
print(f"Estimated Critical Point: {critical_point:.4f}")#round to 4 decimal places
print(f"Function Value at Critical Point: {J(critical_point):.4f}")


#question 2:
def f(w1, w2):
    """Original 2D Function"""
    return (w1 - 8)**2 + (w2 - 8)**2

def J_alpha(alpha):
    """
    1D Function representing the search along direction (1, 2)
    starting from (0, 0).
    w1 = 0 + 1*alpha
    w2 = 0 + 2*alpha
    """
    w1 = alpha
    w2 = 2 * alpha
    return f(w1, w2)

def interval_halving_alpha(a, b, epsilon=0.001, iterations=50):
    """Iteratively finds the best alpha in the range [a, b]"""
    for _ in range(iterations):
        mid = (a + b) / 2
        alpha1 = mid - (epsilon / 2)
        alpha2 = mid + (epsilon / 2)
        
        if J_alpha(alpha1) < J_alpha(alpha2):
            b = alpha2
        else:
            a = alpha1
            
    return (a + b) / 2

# --- Execution ---

# 1. Define a search range for alpha (0 to 10 is plenty here)
lower_alpha = 0
upper_alpha = 10

# 2. Perform the linear search
best_alpha = interval_halving_alpha(lower_alpha, upper_alpha)

# 3. Convert alpha back to w1, w2 coordinates
opt_w1 = best_alpha
opt_w2 = 2 * best_alpha

print(f"Optimal Alpha: {best_alpha:.4f}")
print(f"Optimal Point: ({opt_w1:.4f}, {opt_w2:.4f})")
print(f"Minimum Value: {f(opt_w1, opt_w2):.4f}")

#question 3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 16, 100)
y = np.linspace(0, 16, 100)
X, Y = np.meshgrid(x, y)
Z = (X-8)**2 + (Y-8)**2

plt.contour(X, Y, Z, levels=20)

plt.title("Contour Plot of f(x,y)")
plt.show()

from mpl_toolkits.mplot3d import Axes3D

# 1. Define the function
def f(w1, w2):
    return (w1 - 8)**2 + (w2 - 8)**2

# 2. Create the coordinate grid
w1 = np.linspace(0, 16, 100)
w2 = np.linspace(0, 16, 100)
W1, W2 = np.meshgrid(w1, w2)
Z = f(W1, W2)

# 3. Initialize the plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 4. Plot the surface
# cmap='viridis' gives a nice color gradient based on height
surf = ax.plot_surface(W1, W2, Z, alpha=0.8, edgecolor='none')

# 5. Mark the Global Minimum at (8, 8, 0)
ax.scatter(8, 8, 0, color='red', s=100, label='Minimum (8, 8)', edgecolors='white', zorder=5)

# 6. Labels and Title
ax.set_title('3D Surface Plot of $f(w_1, w_2) = (w_1-8)^2 + (w_2-8)^2$', fontsize=14)
ax.set_xlabel('$w_1$')
ax.set_ylabel('$w_2$')
ax.set_zlabel('$f(w_1, w_2)$')


ax.legend()

plt.show()

import numpy as np
import matplotlib.pyplot as plt

# 1. Setup the Grid and Function
w1 = np.linspace(0, 12, 100)
w2 = np.linspace(0, 12, 100)
W1, W2 = np.meshgrid(w1, w2)
Z = (W1 - 8)**2 + (W2 - 8)**2

# 2. Create the Contour Plot
fig, ax = plt.subplots(figsize=(8, 8))
contours = ax.contour(W1, W2, Z, levels=15)
ax.clabel(contours, inline=True, fontsize=8)


start = [0, 0]
ax.plot(start[0], start[1], label='Start (0,0)') 

# B. The Direction Vector (d = [1, 2])
# quiver(x, y, u, v) draws a vector from (x,y) with components (u,v)
ax.quiver(start[0], start[1], 1, 2, angles='xy', scale_units='xy', scale=1, 
          color='blue', label='Direction d=(1,2)')

# C. The Full Search Path (The line w = alpha * d)
# We plot a line from alpha=0 to alpha=6 to show where the search travels
alphas = np.linspace(0, 6, 100)
path_w1 = 0 + 1 * alphas
path_w2 = 0 + 2 * alphas
ax.plot(path_w1, path_w2, alpha=0.6, label='Search Path')

# The Optimal Point (alpha = 4.8)
opt_w1, opt_w2 = 4.8, 9.6
ax.plot(opt_w1, opt_w2, 'rX', markersize=12, label='Optimal Point (4.8, 9.6)')

# Formatting
ax.set_xlabel('w1')
ax.set_ylabel('w2')
ax.set_title('Contour Plot with Unidirectional Search Direction')
ax.legend()
ax.grid(True, linestyle=':', alpha=0.6)
plt.show()
