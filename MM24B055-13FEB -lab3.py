#qs 1-continue and pass
# # Method 1: Using continue to skip non-matching numbers
# print("Numbers divisible by both 6 and 7 (1-500): continue")

# for i in range(1, 501):
#     if i % 6 != 0 or i % 7 != 0:  # If NOT divisible by both
#         continue  # Skip this iteration-CONTINUE
#     print(i, end=" ")  # This only executes for numbers divisible by both

# # Method 2: Using pass (does nothing)
# print("Numbers divisible by both 6 and 7 (1-500): pass")

# for i in range(1, 501):
#     if i % 6 == 0 and i % 7 == 0:  # If divisible by both
#         print(i, end=" ")
#     else:
#         pass  # Do nothing for non-matching numbers-PASS

#qs2-expansions

# def exp_series(x, terms):
#     result = 1.0
#     term = 1.0
#     for i in range(1, terms):
#         term *= x / i
#         result += term
#     return result

# x = float(input("Enter x: "))
# terms = int(input("Enter number of terms: "))
# print(f"exp({x}) = {exp_series(x, terms)}")

# def sin_series(x, terms):
#     result = 0.0
#     term = x
#     for i in range(1, terms + 1):
#         sign = 1 if i % 2 else -1
#         result += sign * term
#         term *= x * x / ((2*i) * (2*i + 1))
#     return result

# x = float(input("Enter x: "))
# terms = int(input("Enter number of terms: "))
# print(f"sin({x}) = {sin_series(x, terms)}")

# def cos_series(x, terms):
#     result = 0.0
#     term = 1.0
#     for i in range(terms):
#         sign = 1 if i % 2 == 0 else -1
#         result += sign * term
#         term *= x * x / ((2*i + 1) * (2*i + 2))
#     return result

# x = float(input("Enter x: "))
# terms = int(input("Enter number of terms: "))
# print(f"cos({x}) = {cos_series(x, terms)}")

#qs3 list op
# accounts = ["Rahul", "Priya", "Amit", "Neha", "Vikram"]
# print("Initial:", accounts)

# while True:
#     choice = input("\n1.Insert 2.Delete 3.AddFirst 4.Unique 5.Sort 6.Show 7.Exit: ")
    
#     if choice == '1':
#         name = input("Name: ")
#         accounts.append(name)
#         accounts.sort()
    
#     elif choice == '2':
#         name = input("Delete: ")
#         if name in accounts: accounts.remove(name)
    
#     elif choice == '3':
#         accounts.insert(0, input("Add first: "))
    
#     elif choice == '4':
#         unique = []
#         for n in accounts:
#             if n not in unique: unique.append(n)
#         accounts = unique
    
#     elif choice == '5':
#         accounts.sort()
    
#     elif choice == '6':
#         print(accounts)
    
#     elif choice == '7':
#         break

# #list comprehension (qs 4)
# list2=[22,34,5,78]

# sumlist=[list1[i]+list2[i] for i in range (len(list1))]
# print(sumlist)

# productlist=[list1[i]*list2[i] for i in range (len(list1))]
# print(productlist)

# input_str =input("enter the input string")
# unique_chars = []
# [unique_chars.append(char) for char in input_str if char not in unique_chars]
# print(unique_chars)  # ['e', 'v', 'n']


#qs5-median and indexing
# import random

# Create list of random integers in range(1,100)
# n = int(input("Enter number of elements: "))
# numbers = [random.randint(1, 99) for _ in range(n)]
# print("Original list:", numbers)

# # Find median
# sorted_numbers = sorted(numbers)
# length = len(sorted_numbers)

# if length % 2 == 0:
#     # Even length: median is average of middle two
#     median = (sorted_numbers[length//2 - 1] + sorted_numbers[length//2]) / 2
#     mid1 = length//2
#     mid2 = length//2
# else:
#     # Odd length: median is middle element
#     median = sorted_numbers[length//2]
#     mid1 = length//2
#     mid2 = length//2 + 1

# print(f"Median: {median}")

# # Divide into two sublists with respect to median
# list1 = sorted_numbers[:mid1]
# list2 = sorted_numbers[mid2:]

# print("First sublist :", list1)
# print("Second sublist :", list2)

# # list comprehension and random number generation:(qs 6)
# import random
# random_numbers = [random.randint(10, 100) for _ in range(20)]
# print(f"All random numbers: {random_numbers}")

# # (a) Print even numbers
# even_numbers = [num for num in random_numbers if num % 2 == 0]
# print(f"Even numbers: {even_numbers}")

# # (b) Print odd numbers
# odd_numbers = [num for num in random_numbers if num % 2 != 0]
# print(f"Odd numbers: {odd_numbers}")

#qs7-transpose
# Sample matrices (remove input for quick testing)
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("A:", A)
print("B:", B)

# All operations without zip()
print("\nWithout zip():")
print("Transpose A:", [[A[j][i] for j in range(3)] for i in range(3)])
print("Transpose B:", [[B[j][i] for j in range(3)] for i in range(3)])
print("A + B:", [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)])
print("A - B:", [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)])
print("Trace A:", sum(A[i][i] for i in range(3)))
print("Trace B:", sum(B[i][i] for i in range(3)))

# All operations with list comprehension (but still without zip)
print("\nWith list comprehension:")
print("Transpose A:", [[row[i] for row in A] for i in range(3)])
print("Addition:", [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)])
print("Subtraction:", [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)])

#qs 8
# Take matrix input
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(3)] for i in range(3)]
print("Original:", A)

# Swap rows
r1, r2 = map(int, input("Enter rows to swap (r1 r2): ").split())
A[r1], A[r2] = A[r2], A[r1]
print("After row swap:", A)

# Swap columns
c1, c2 = map(int, input("Enter columns to swap (c1 c2): ").split())
for i in range(len(A)):
    A[i][c1], A[i][c2] = A[i][c2], A[i][c1]
print("After column swap:", A)


# #qs 9
# nums1 = [3, 8, 12, 4, 7, 9] 
# nums2 = [5, 1, 9, 14, 6, 3]

# target=int(input("enter the target sum"))
# Pairfound=False

            
# for i in range (len(nums2)):
#     for j in range(2,len(nums2)):
#         if nums2[i]+nums2[j]==target:
#            Pairfound=True 
# if Pairfound:
#     print("pair found")
# else:
#     print("no pair found")
    
# # for i in  range (len(nums1)):
# #     for j in range(len(nums2)):
# #         if nums1[i]+nums2[j]==target:
# #           Pairfound=True
# # if Pairfound:
# #     print("pair found")
# # else:
# #     print("no pair found")
        

