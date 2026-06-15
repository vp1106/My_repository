# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:08:01 2026

@author: veda pramod
"""
#Lab 7 – Files, Pandas, Operator Overloading, Multiple Inheritance, and Plotting

#question 6

# import numpy as np #numerical python
# import matplotlib.pyplot as plt #matplot lib imported

# # Range for cos(x) and e^x
# x = np.linspace(-10, 10, 400)#linspace used to create a uniform array of x values
# # Range for log(x)
# x_log = np.linspace(0.1, 10, 400)# log is defined only for positive x value not even for zero so we go from 0.1

# # Function values(np has inbuilt functions)
# y_cos = np.cos(x)
# y_exp = np.exp(x)
# y_log = np.log(x_log)

# # Plot a) y = cos(x)
# plt.subplot(3, 1, 1)#plt.sublot(rows,colums,index)-to compare all three in the same window
# plt.plot(x, y_cos, label='$y = \\cos(x)$', color='blue')
# plt.title('Plot of $y = \\cos(x)$')
# plt.xlabel('$x$')#jus labels
# plt.ylabel('$y$')
# plt.grid(True)#for grid to be displayed

# # Plot b) y = e^x
# plt.subplot(3, 1, 2)
# plt.plot(x, y_exp, label='$y = e^x$', color='red')
# plt.title('Plot of $y = e^x$')
# plt.xlabel('$x$')
# plt.ylabel('$y$')
# plt.grid(True)

# # Plot c) y = log(x)
# plt.subplot(3, 1, 3)
# plt.plot(x_log, y_log, label='$y = \\ln(x)$', color='green')
# plt.title('Plot of $y = \\log(x)$')
# plt.xlabel('$x$')
# plt.ylabel('$y$')
# plt.grid(True) 

# # Adjust layout and save
# plt.tight_layout()
# plt.show()
# # required for u to see the output in the plots 
# plt.savefig('mathematical_functions.png')


#question 5

# import pandas as pd
# import matplotlib.pyplot as plt

# # The provided sales data
# sales_data = {
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
#     "Product_A": [120, 150, 170, 160, 180],
#     "Product_B": [90, 110, 130, 120, 140],
#     "Product_C": [60, 80, 100, 95, 105]
# }

# # a) Convert to DataFrame
# df = pd.DataFrame(sales_data)

# # b) Calculate total sales for each product
# # We sum vertically (axis=0) across the rows for each column
# product_totals = df[["Product_A", "Product_B", "Product_C"]].sum(axis=0)

# print("Total Sales per Product:")
# print(product_totals)

# # c) Create a bar chart
# plt.figure(figsize=(8, 6))

# # Use the names of the products (index) and the calculated totals (values)
# plt.bar(product_totals.index, product_totals.values, color='skyblue', edgecolor='black')

# plt.title('Total Sales by Product (Jan-May)')
# plt.xlabel('Product')
# plt.ylabel('Total Units Sold')
# plt.grid(axis='y', linestyle='--', alpha=0.7)

# plt.show()

#question 4

# class Notebook:
#     def __init__(self,title="",content=""):
#         self.__title=""
#         self.__content=""
        
#     def AddNewNote(self):
#         with open('notes.txt','w') as f:
#             self.__title=str(input("pls enter the title"))
#             self.__content=str(input("pls enter the content to bbe written on the file"))
#             f.write(self.__title)
#             f.write(self.__content)

#     def DisplayNotes(self):
#         with open('notes.txt','r') as f:
#             data=f.read()
#             print(data)
            
#     def MenuInterface(self):
#         print("menu interface")
#         print("option 1 : Addnewnote")
#         print("option 2: DisplayNotes")
#         option=int(input("pls enter your option"))
#         if option==1:
#             self.AddNewNote()
#         elif option==2:
#             self.DisplayNotes()
#         else:
#             print("enter valid option//")
            
# #main
# mynote=Notebook()
# mynote.MenuInterface()

#question 3

# import csv
# import os

# # Configuration
# FILE_NAME = "books.csv"
# HEADERS = ["Title", "Author", "Publication Year", "ISBN"]

# def initialize_file():
#     """Creates the file with headers if it doesn't already exist."""
#     if not os.path.exists(FILE_NAME):
#         with open(FILE_NAME, 'w', newline='') as f:
#             writer = csv.writer(f)
#             writer.writerow(HEADERS)
#         print(f"File '{FILE_NAME}' created successfully.")

# def add_book():
#     """Prompts for input and appends to the CSV file."""
#     title = input("Enter Title: ")
#     author = input("Enter Author: ")
#     year = input("Enter Publication Year: ")
#     isbn = input("Enter ISBN Number: ")

#     with open(FILE_NAME, 'a', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow([title, author, year, isbn])#synatx for adding to csv file...
#     print("Book added successfully!\n")

# def display_books():
#     """Reads and prints all books from the CSV file."""
#     if not os.path.exists(FILE_NAME):
#         print("No records found.")
#         return
#     with open(FILE_NAME, 'r') as f:
#         reader = csv.reader(f)
#         next(reader)  # Skip the header row
#         for row in reader:
#             print(row)
#     print()

# # Main Menu
# initialize_file()
# while True:
#     print("1. Add New Book\n2. Display All Books\n3. Exit")
#     choice = input("Select an option: ")
#     if choice == '1': add_book()
#     elif choice == '2': display_books()
#     elif choice == '3': break
            
# import random

# class Matrix:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         # Store matrix as a list of lists using list comprehension
#         self.data = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

#     def __add__(self, other):
#         """Overloads the + operator for Matrix Addition."""
#         result = Matrix(self.rows, self.cols)
#         result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
#         return result

#     def __sub__(self, other):
#         """Overloads the - operator for Matrix Subtraction."""
#         result = Matrix(self.rows, self.cols)
#         result.data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
#         return result

#     def __mul__(self, other):
#         """Overloads the * operator. Performs Matrix Multiplication if 'other' is a Matrix, 
#         or Scalar Multiplication if 'other' is an int/float."""
#         if isinstance(other, Matrix):
#             if self.cols != other.rows:
#                 raise ValueError("Incompatible dimensions for matrix multiplication.")
#             result = Matrix(self.rows, other.cols)
#             result.data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) 
#                             for j in range(other.cols)] for i in range(self.rows)]
#             return result
#         elif isinstance(other, (int, float)):
#             # Scalar multiplication using map()
#             result = Matrix(self.rows, self.cols)
#             result.data = [list(map(lambda x: x * other, row)) for row in self.data]
#             return result

#     def element_wise_mul(self, other):
#         result = Matrix(self.rows, self.cols)
#         result.data = [[self.data[i][j] * other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
#         return result

#     def __str__(self):
#         return '\n'.join([' '.join(map(str, row)) for row in self.data])
#main
# m1 = Matrix(2, 2)
# m2 = Matrix(2, 2)
# print("Matrix 1:\n", m1)
# print("\nMatrix 2:\n", m2)
# print("\nAddition:\n", m1 + m2)
# print("\nScalar Multiplication (m1 * 2):\n", m1 * 2)


# import json

# FILE_NAME = 'employees.json'

# def load_data():
#     """Reads the JSON file and returns the data dictionary."""
#     with open(FILE_NAME, 'r') as file:
#         return json.load(file)

# def save_data(data):
#     """Saves the updated dictionary back to the JSON file."""
#     with open(FILE_NAME, 'w') as file:
#         json.dump(data, file, indent=4)

# def display_all():
#     """a) Displays all employees."""
#     data = load_data()
#     for emp in data['employees']:
#         print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['department']}")

# def search_by_id(emp_id):
#     """b) Searches for employee by ID."""
#     data = load_data()
#     for emp in data['employees']:
#         if emp['id'] == emp_id:
#             print(f"Found: {emp}")
#             return
#     print("Employee not found.")

# def add_employee():
#     """c) Adds a new employee and saves to file."""
#     data = load_data()
#     new_id = int(input("Enter ID: "))
#     name = input("Enter Name: ")
#     age = int(input("Enter Age: "))
#     dept = input("Enter Department: ")
#     skills = input("Enter skills (comma-separated): ").split(',')
    
#     new_emp = {
#         "id": new_id,
#         "name": name,
#         "age": age,
#         "department": dept,
#         "skills": [s.strip() for s in skills]
#     }
    
#     data['employees'].append(new_emp)
#     save_data(data)
#     print("Employee added successfully!")

# # Basic Menu Interface
# if __name__ == "__main__":
#     display_all()
#     # add_employee() # Uncomment to test adding
            
            
            


