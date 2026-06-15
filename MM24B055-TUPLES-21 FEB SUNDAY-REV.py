# # Tuples

# empty_tup=tuple()
# tup1=(10,)
# tup2=('ram',23,4.5,[1,2,3])
# print(tup1,tup2,sep="\n\n")#damn use these to print extra lines

# #print(tup1,end="\n",tup2,end="\n")#will throw an error coz end="\n" 
# #is a keyword argument and pos arguments must be before that any pos after will show error

# #elements in tuple can be repeated
# Tuple_dup=(23,33,45,45,67)
# print(Tuple_dup)

# #tuples are sequential can be indexed and sliced.
# mytuple=(23,"veda","happy","mummy",29.5,15,67,96,[1,2,3,4],(0.5,{1,2,3}))
# reversed_tuple=tuple(list(mytuple[::-1]))#damn bro it worked
# print(reversed_tuple)

# #entire tuple or each element can be printed
# for i in mytuple:
#     print(i)
# for index,item in enumerate(mytuple):
#     print(index,item)

# #tuple is an iterable you can iterate over its elements
# #print every alternate item i tuple
# for i in range(0,len(mytuple),2):
#     print(mytuple[i])    #common error in tuple-use mytuple[i] not mytuple(i-error ot callable-due to parantheses-thinks its a func)

# #CW: Define a tuple of different datatypes and print them using iterator. 
# for i,item in enumerate(mytuple):
#     print(f"this item {item} ,is of type",type(item).__name__)
    
# #HW:In a tuple, find the number of objects of each type.
# #dictionary will be much easier?

# def count_types(tup):
#     type_count = {}
    
#     for item in tup:
#         # Get the type name as string
#         item_type = type(item).__name__
        
#         # Count occurrences
#         if item_type in type_count:# this si the main condition -u should remember///
#             type_count[item_type] += 1
#         else:
#             type_count[item_type] = 1
    
#     return type_count

# # Example usage
# my_tuple = (1, "hello", 3.14, True, "world", 42, 3.14, False, [1,2], "python", 10)
# result = count_types(my_tuple)

# # what is there are a lot of nested things???

# # Print results
# for type_name, count in result.items():
#     print(f"{type_name}: {count}")
    
# #tuple operations:

# #tuples are immutable?
# #mytuple[2]="viba"
# print(mytuple)# throws error  doest support assignment

# #tuples can be concatenated
# new_tup=my_tuple+mytuple
# print(new_tup)

# #searching(containment) and sorting?
# search_item=int(input("enter the search item"))
# #if i just give number 42 without the int then it takes 42 as string and says not found
# # what can be done???
# for item in new_tup:
#     if item==search_item:
#         print("found")

# #deletion using list of range of indices-no delete functio as such
# new_tup=new_tup[5:]
# print(new_tup)

# #conversion from str t tuple?
# name_tup=tuple("veda")
# print(name_tup)

# #directly done noice

# #len max min sum all of them work in tuple...

# #index and count are member functions of tuple

# i=mytuple.index(67)
# print(i)

# ct=new_tup.count(42)
# print(ct)

# #tuple cmparison???
# #element wise comparison
# print((1,2,3)<(1,22,3))
# # Comparison stops at the first differing element

# print((1, 2) < (1, 2, 3))        # True - shorter is considered smaller
# print((1, 'a') < (1, 'b'))        # True - 'a' < 'b'

# # Nested tuples are compared recursively
# tuple1 = (1, (2, 3), 4)
# tuple2 = (1, (2, 4), 4)
# tuple3 = (1, (2, 3), 5)

# print(f"tuple1: {tuple1}")
# print(f"tuple2: {tuple2}")
# print(f"tuple3: {tuple3}")
# print()

# print(f"tuple1 == tuple2: {tuple1 == tuple2}")  # False (compares (2,3) vs (2,4))
# print(f"tuple1 < tuple2: {tuple1 < tuple2}")    # True (3 < 4 in nested tuple)
# print(f"tuple1 < tuple3: {tuple1 < tuple3}")    # True (4 < 5)


#HW: Find out the functions that are not in tuples but available in lists and why?
#tuple(),count(),index()

#no tuple comprehension do list comprehension and use tuple()-it becomes a generator expression

# #use * operator?


# # nested_tuple=((1,2),3,4,5,(6,7),8,9,10)
# # print(*nested_tuple)

# nested_tuple = ((1,2), 3, 4, 5, (6,7), 8, 9, 10)

# for element in nested_tuple:
#     if isinstance(element, tuple):#checks if that element is tuple-ohhhh
#         for inner_element in element:
#             print(inner_element)
#     else:
#         print(element)

# #for ay depth-recursion???

# def print_all_elements(item):
#     if isinstance(item, tuple) or isinstance(item,list) or isinstance(item,set):
#         for sub_item in item:
#             print_all_elements(sub_item)
#     else:
#         print(item)

# nested_tuple = ((1,2), 3, 4, 5, (6,7), 8, 9, 10)
# print_all_elements(nested_tuple)

# #grouping tuples\
# # fruits = ('apples', 'oranges', 'grapes', 'guava')
# # num_kg = (2, 5, 3, 6)
# # cost_kg = (150, 80, 200, 170)

# # newlist=[(x,y,z) for x in fruits for y in num_kg for z in cost_kg]

# fruits = ('apples', 'oranges', 'grapes', 'guava')
# num_kg = (2, 5, 3, 6)
# cost_kg = (150, 80, 200, 170)

# # Method 1: Using zip() with list comprehension (RECOMMENDED)
# newlist = [(fruits[i], num_kg[i], cost_kg[i]) for i in range(len(fruits))]
# print(newlist)
# # Output: [('apples', 2, 150), ('oranges', 5, 80), ('grapes', 3, 200), ('guava', 6, 170)]

# # Method 2: More Pythonic with zip()
# newlist = tuple(zip(fruits, num_kg, cost_kg))
# print(newlist)
# # Output: [('apples', 2, 150), ('oranges', 5, 80), ('grapes', 3, 200), ('guava', 6, 170)]


# names = ('Ram', 'Raja', 'Geetha', 'Ramya')
# gender = ('male', 'male', 'female', 'female')
# ite = zip(names, gender)
# print(type(ite).__name__)#zip is a fucking datatype?
# print(*ite)  
# # Output: ('Ram', 'male') ('Raja', 'male') ('Geetha', 'female') ('Ramya', 'female')

# #zip() iterator works like a pointer that moves through the data. Let me explain with simple examples:
    
# names = ('Ram', 'Raja', 'Geetha', 'Ramya')
# gender = ('male', 'male', 'female', 'female')

# # # Create iterator (like a pointer)
# # ite = zip(names, gender)

# # # Each time we use it, it moves to the next item
# # print(next(ite))  # ('Ram', 'male')    ← ite now points to first pair
# # print(next(ite))  # ('Raja', 'male')   ← ite moves to second pair
# # print(next(ite))  # ('Geetha', 'female') ← moves to third pair
# # print(next(ite))  # ('Ramya', 'female')  ← moves to fourth pair
# # # print(next(ite))  # StopIteration error - no more items!

# #CW: Take three lists, one each for few names, their 
# #ages and salaries and make a tuple out of the lists.

# names = ['Ram', 'Raja', 'Geetha', 'Ramya']
# age=[23,34,28,35]
# salary=[25000,24000,78000,12000]
# employee_details=tuple(zip(names,age,salary))
# print(*employee_details)

# #HW: WAP to print the transpose of a 3X5 matrix. 

# #many methods for this...

# # Original 3×5 matrix (3 rows, 5 columns)
# matrix = [
#     [1,  2,  3,  4,  5],
#     [6,  7,  8,  9, 10],
#     [11, 12, 13, 14, 15]
# ]

# print("Original Matrix (3×5):")
# for row in matrix:
#     print(row)

# # Transpose to 5×3 matrix
# print("\nTranspose Matrix (5×3):")
# for col in range(5):  # 5 columns in original = 5 rows in transpose
#     transpose_row = []
#     for row in range(3):  # 3 rows in original = 3 columns in transpose
#         transpose_row.append(matrix[row][col])
#     print(transpose_row)
# #list comprehension


# matrix = [
#     [1,  2,  3,  4,  5],
#     [6,  7,  8,  9, 10],
#     [11, 12, 13, 14, 15]
# ]

# print("Original Matrix:")
# for row in matrix:
#     print(row)

# # Transpose using list comprehension
# transpose = [[matrix[row][col] for row in range(3)] for col in range(5)]

# print("\nTranspose Matrix:")
# for row in transpose:
#     print(row)
    
# #ulla irukarthu 3 times veliya 5 times u wat 5 rows u give 3 rows and u wat 3 columnns u give 5 columns)-row column conv stays says

# # zip function

# matrix = [
#     [1,  2,  3,  4,  5],
#     [6,  7,  8,  9, 10],
#     [11, 12, 13, 14, 15]
# ]

# print("Original Matrix:")
# for row in matrix:
#     print(row)

# # Transpose using zip() - unpacks rows and zips them column-wise
# transpose = list(zip(*matrix))

# print("\nTranspose Matrix:")
# for row in transpose:
#     print(row) 
    
#     #easy as f
    
# import numpy as np

# matrix = np.array([#array module///
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15]
# ])

# print("Original Matrix:")
# print(matrix)
# print("\nTranspose Matrix:")
# print(matrix.T)




