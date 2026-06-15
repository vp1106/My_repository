# WEDNESDAY 11 TH MARCH

import numpy as np
import matplotlib.pyplot as plt # You need this to use 'plt'

# # # 1. Generate the data
# x = np.linspace(-5, 5, 100)
# y = x**3

# x1=np.linspace(-5,5,100)
# y1=x**2
# # 2. Create the plot
# plt.plot(x, y)

# # 3. Add context (Optional but helpful)
# plt.title('Parabola: $y = x^2$')#title
# plt.xlabel('x values')#x label
# plt.ylabel('y values')#y label
# plt.grid(True)

# 4. Show the result
#plt.show()

# plt.plot(x, y, 'o--')
# plt.plot(x, y, 'o')
# plt.plot(x, y, 'o--', color='red', lw = 2.5, ms = 5)
# plt.show()

#multiple axis figure
# m_fig, m_axes = plt.subplots(2, 2, figsize = (8,4))
# ax = m_axes[0][0]
# ax.plot(x,y)
# ax.set(xlabel='x vlues', ylabel='y values',
#         title='Explicit function y = f(x)')
# ax = m_axes[0][1]
# ax.plot(x1,y1)
# ax.set(xlabel='x vlues', ylabel='y values',
#         title='Explicit function y = f(x)')
# plt.show()

# Parametric space curve t, t**2, t**3
# t = np.arange(-2.0, 2.0, 0.1) #the parameter
# x = t
# y = t ** 3
# z = t ** 3
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x, y, z)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# ax.set_title('Parametric space curve t, t**2, t**3')
# plt.show()


x = np.arange(-2.0, 2.0, 0.1)
y = np.arange(-2.0, 2.0, 0.1)
# The following will print a 3D surface
X,Y=np.meshgrid(x,y) #Forming MeshGrid
Z = X **2 + Y ** 2
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# plt.show()

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(X, Y, Z)
cp  = plt.contour(x, y, Z)
plt.clabel(cp, fontsize=8)
plt.show()