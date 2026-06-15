# #Dictionaries
# #22 feb

# #dictionary is a always a key value pair?
# mydict={}
# print(type(mydict).__name__)
# #empty braces is not set but a dict

# #dictionary indexed only by keys
# student={
#        "name":"Alice",# usse: not =
#         "age":20,
#         "Grade":"A"
#         }
# print(student["name"])
# print(student["age"])
# print(student["Grade"])# double quotes for keys use sqr braces

# print(student)
# #print(student[0])
# # raises a key error searches for key zero doesnt work -key error

# #why no indexing
# #data stored at a memory location based on hashing-so if exact same keyword not given then cannot find the same location
# print(student.keys())
# print(student.items())
# print(student.values())#values not value

# #dict function constructor
# # Using keyword arguments
# person = dict(name="Bob", age=25, job="Engineer", city="Boston")
# print(person)

# # Using list of tuples
# person = dict([("name", "Bob"), ("age", 25), ("job", "Engineer")])
# print(person)

# #dict () only works with string keys that are valid identifiers
# #marks=dict("1":"25","2":"15")# error

# #print(marks.values())
# marks = {"1": "25", "2": "15"}
# print(marks)  # {'1': '25', '2': '15'}

# marks = dict([("1", "25"), ("2", "15")])
# print(marks)  # {'1': '25', '2': '15'}

# keys = ["1", "2"]
# values = ["25", "15"]
# marks = dict(zip(keys, values))
# print(marks)  # {'1': '25', '2': '15'}



# #keys in dictionary must be unique and immutable///
# #this is because the data is stored in the memory location by hashing the value of the key
# #so unhashable types like set,dict,list cannot be used as a key-muatble type as well
# #tuples can be used but it shouldnt have an mutable type inside it
# from collections.abc import Hashable

# def can_be_key(obj):
#     return isinstance(obj, Hashable)

# # Create dictionary with default value None
# keys = ['name', 'age', 'city']
# result = dict.fromkeys(keys)
# print(result)  # {'name': None, 'age': None, 'city': None}

# # With a specified default value
# result = dict.fromkeys(keys, 'unknown')
# print(result)  # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# # Define the dictionary
# student = {
#     "name": "Ramanathan Muthuganapath",
#     "age": 25,
#     "course": "Computer Science",
#     "grade": "A",
#     "city": "Chennai"
# }

# # Print all values using keys in a loop
# print("Student Details:")
# for key in student:
#     print(f"{key.capitalize()}: {student[key]}")#capitalize func
    
# #dictionaries are mutable

# student["grade"]="D"#lool
# print(student)    

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

# # This will NOT work
# # result = dict1 + dict2  # ❌ TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# dict1.update(dict2)
# print(dict1)

# merged=student|dict1 #like union
# print(merged)

#sorting of dictionaries

# fruits={
#         "chikoo":43,
#         "apple":23,
#         "banana":24,
#         "watermelon":35
#         }
# # sorted_fruits=sorted(fruits.keys())#sorts only keys
# # print(sorted_fruits)
# # for name in sorted_fruits:
# #     print(f"{name}:{fruits[name]}")
    
    
# # sorted_fruits=dict(sorted(fruits.items()))
# # print(sorted_fruits)

# # qtsorted=dict(sorted(fruits.items(),key=lambda x:x[1]))
# # print(qtsorted)

# qtsorted=dict(sorted(fruits.items(),key=lambda x:x[1],reverse=True))
# print(qtsorted)

# print(sorted(fruits.keys()))
# print(sorted(fruits.values()))

#dictionary comprehension

fruits=["apple","chikoo","banana"]
price=[65,23,45]

# fruit_prices={}#dict
# for i in range (len(fruits)):
    
#     fruit_prices[fruits[i]]=price[i]
# print(fruit_prices)


# fruit_prices={fruits[i]:price[i] for i in range( len(fruits))}
# print(fruit_prices)

#or use zip///
fruit_prices={fruits:price for fruits,price in zip(fruits,price)}
print(fruit_prices)
