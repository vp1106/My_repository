#FRIDAY LAB CLASS

#question 1
# class Car:
#     def __init__(self, make, model, year):
#         self.Make = make
#         self.Model = model
#         self.Year = year
        
#     def DisplayCarDetails(self):
#         print("Car Make:", self.Make)
#         print("Car Model:", self.Model)
#         print("Car Year:", self.Year)
        
# # Test the Car class
# Mycar = Car("Volkswagen", "Golf", 1984)
# Mycar.DisplayCarDetails()

#question 2

# import math

# class Complex:
#     def __init__(self, real=0, imag=0):
#         self.real = real
#         self.imag = imag
    
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
    
#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)
    
#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag
#         imag_part = self.imag * other.real + self.real * other.imag
#         return Complex(real_part, imag_part)
    
#     def __str__(self):
#         if self.imag >= 0:
#             return f"{self.real} + {self.imag}i"
#         else:
#             return f"{self.real} - {abs(self.imag)}i"


# class PolarComplex(Complex):
#     def __init__(self, real=0, imag=0):
#         super().__init__(real, imag)
#         self.r = math.sqrt(real**2 + imag**2)
#         self.theta = math.atan2(imag, real)
    
#     @classmethod
#     def from_polar(cls, r, theta):
#         real = r * math.cos(theta)
#         imag = r * math.sin(theta)
#         return cls(real, imag)
    
#     def __mul__(self, other):
#         new_r = self.r * other.r
#         new_theta = self.theta + other.theta
#         return PolarComplex.from_polar(new_r, new_theta)
    
#     def __str__(self):
#         return f"{self.real} + {self.imag}i (r={self.r:.2f}, θ={self.theta:.2f})"


# # Create from rectangular coordinates
# pc1 = PolarComplex(3, 4)
# print(f"pc1 = {pc1}")

# # Create from polar coordinates
# pc2 = PolarComplex.from_polar(2, math.pi/6)  # r=2, angle=30°
# print(f"pc2 = {pc2}")

# # Multiply them
# pc3 = pc1 * pc2
# print(f"pc1 * pc2 = {pc3}")

# # Verify by multiplying original complex numbers
# print("\nVerification with regular Complex:")
# c1 = Complex(3, 4)
# c2 = Complex(2*math.cos(math.pi/6), 2*math.sin(math.pi/6))
# c3 = c1 * c2
# print(f"c1 * c2 = {c3}")  


# #question 3

class Polynomial:
    def __init__(self, coefficients):
        # [7, 0, 4, 3] -> 7 + 0x + 4x^2 + 3x^3
        self.coeffs = coefficients

    def __sub__(self, other):
        # Determine the maximum degree between the two
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = []
        
        for i in range(max_len):
            # Get coeff from self, default to 0 if index is out of range
            val1 = self.coeffs[i] if i < len(self.coeffs) else 0
            # Get coeff from other, default to 0 if index is out of range
            val2 = other.coeffs[i] if i < len(other.coeffs) else 0
            new_coeffs.append(val1 - val2)
            
        return Polynomial(new_coeffs)

    def __repr__(self):
        if not self.coeffs or all(c == 0 for c in self.coeffs):
            return "0"
        terms = []
        for i, c in enumerate(self.coeffs):
            if c == 0: continue
            if i == 0: terms.append(str(c))
            elif i == 1: terms.append(f"{c}x")
            else: terms.append(f"{c}x^{i}")
        return " + ".join(terms)
    
class DerivativePolynomial(Polynomial):
    def get_derivative(self):
        # If it's just a constant, derivative is 0
        if len(self.coeffs) <= 1:
            return Polynomial([0])
            
        # d/dx of (c*x^i) is (i*c)*x^(i-1)
        # We start from index 1 (the x^1 term)
        derived_coeffs = []
        for i in range(1, len(self.coeffs)):
            derived_coeffs.append(i * self.coeffs[i])
            
        return Polynomial(derived_coeffs)

    # c) Overriding subtraction to find the difference between derivatives
    def __sub__(self, other):
        # Calculate the derivatives first
        deriv1 = self.get_derivative()
        deriv2 = other.get_derivative()
        
        # Use the logic from the parent (Polynomial) class to subtract them
        # We call Polynomial.__sub__ specifically to avoid infinite recursion
        return Polynomial.__sub__(deriv1, deriv2)
    
    
#Question 6
# with open('userdata.txt', 'w') as f:
#     f.write('')  # Write nothing
# with open('userdata.txt', 'a') as f:
#     f.write("user data")
#     f.write("\n")
#     count=int(input("enter the number of users you want to save?"))
#     for i in range(count):
#        name=input("enter name of user")
#        f.write(str(name+"\n"))
#        age=int(input("enter the age"))
#        f.write(str(str(age)+"\n"))
#        city=input("enetr the city")
#        f.write(str(city+"\n"))
      
# f= open('userdata.txt','r')# no colon after that
# userdata=f.read()
# print(userdata)
# f.close()
 
# question 5

# # Using 'with' (auto-closes the file)
# with open('userdata.txt', 'r') as file:#not using sample coz no such file-doin it for userdata instead
#     content = file.read()
#     words = content.split()#that was easy
#     word_count = len(words)+1

# print("Number of words:", word_count)   

# # Read the file
# with open('userdata.txt', 'r') as file:
#     content = file.read()

# # Split into words
# words = content.split()

# # Count occurrences using dictionary
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
            
# # Display results
# print("Word occurrences:")
# for word, count in word_count.items():
#     print(f"'{word}': {count}")

 #question 4:
     
# import math

# class Vector:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z

#     # iv) Operator overloading for '+'
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

#     # i) Subtraction
#     def subvectors(self, other):
#         return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

#     # i) Dot Product: (x1*x2 + y1*y2 + z1*z2) -> Results in a scalar
#     def dotproduct(self, other):
#         return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

#     # i) Cross Product
#     def crossproduct(self, other):
        
#         nx = self.y * other.z - self.z * other.y
#         ny = self.z * other.x - self.x * other.z
#         nz = self.x * other.y - self.y * other.x
#         return Vector(nx, ny, nz)

#     # ii) Scalar multiplication
#     def scalarmultiply(self, scalar):
#         return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

#     # iii) Magnitude calculation: sqrt(x^2 + y^2 + z^2)
#     def magnitudecalc(self):
#         return (self.x**2 + self.y**2 + self.z**2)**0.5

#     # iv) Operator overloading for '==' and '<'
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y and self.z == other.z

#     def __lt__(self, other):
#         return self.magnitudecalc() < other.magnitudecalc()

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y}, {self.z})"
 
    
# print("Enter coordinates for Vector 1 (format: x y z):")
# x1, y1, z1 = map(float, input().split())
# v1 = Vector(x1, y1, z1)

# print("Enter coordinates for Vector 2 (format: x y z):")
# x2, y2, z2 = map(float, input().split())
# v2 = Vector(x2, y2, z2)


# print(f"Vector 1: {v1}")
# print(f"Vector 2: {v2}")
# print(f"Addition (v1 + v2): {v1 + v2}")  # Uses __add__
# print(f"Subtraction: {v1.subvectors(v2)}")
# print(f"Dot Product: {v1.dotproduct(v2)}")
# print(f"Cross Product: {v1.crossproduct(v2)}")
# print(f"Scalar Multi (v1 * 3): {v1.scalarmultiply(3)}")
# print(f"Magnitude of v1: {v1.magnitudecalc():.2f}")

# print(f"Is v1 == v2? {v1 == v2}")
# print(f"Is v1 < v2 (by magnitude)? {v1 < v2}")
       
    
       