# QS 5 LAB

# a) Create a dictionary with 5 key-value pairs
student = {
    'name': 'Alice',
    'age': 20,
    'course': 'Computer Science',
    'grade': 'A',
    'city': 'New York'
}

print("\na) Dictionary created:")
print(student)

# b) Access a value using a key
print("\nb) Accessing values:")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")

# c) Add a new key-value pair
print("\nc) Adding new key-value pair:")
student['phone'] = '123-456-7890'
print(f"After adding phone: {student}")

# d) Update an existing value
print("\nd) Updating existing value:")
student['grade'] = 'A+'
print(f"After updating grade: {student}")

# e) Delete a key from the dictionary
print("\ne) Deleting a key:")
del student['phone']
print(f"After deleting phone: {student}")

# f) Count frequency of each character in a string
print("\nf) Character frequency:")
text = "hello world"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(f"String: '{text}'")
print(f"Character frequency: {freq}")

# g) Merge two dictionaries
print("\ng) Merging dictionaries:")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}  # Using unpacking
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"Merged: {merged}")

# h) Print all keys and values separately
print("\nh) Keys and values separately:")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")

# i) Sort a dictionary by its keys
print("\ni) Sort dictionary by keys:")
unsorted = {'z': 26, 'b': 2, 'a': 1, 'c': 3}
sorted_dict = dict(sorted(unsorted.items()))
print(f"Unsorted: {unsorted}")
print(f"Sorted by keys: {sorted_dict}")

# j) Check whether a given key exists
print("\nj) Check key existence:")
key_to_check = 'name'
if key_to_check in student:
    print(f"Key '{key_to_check}' exists in dictionary")
else:
    print(f"Key '{key_to_check}' does not exist")

key_to_check = 'phone'
if key_to_check in student:
    print(f"Key '{key_to_check}' exists in dictionary")
else:
    print(f"Key '{key_to_check}' does not exist")

print("\n" + "="*50)
print("ADDITIONAL EXAMPLES")
print("="*50)

# All operations on a single example
print("\nWorking with a number dictionary:")

# Create
nums = {'one': 1, 'two': 2, 'three': 3}
print(f"Created: {nums}")

# Access
print(f"Value of 'two': {nums['two']}")

# Add
nums['four'] = 4
print(f"After adding: {nums}")

# Update
nums['three'] = 33
print(f"After updating: {nums}")

# Delete
del nums['two']
print(f"After deleting: {nums}")

# Character frequency (another example)
word = "programming"
freq2 = {}
for c in word:
    freq2[c] = freq2.get(c, 0) + 1
print(f"\nFrequency of '{word}': {freq2}")

# Merge
more_nums = {'five': 5, 'six': 6}
all_nums = {**nums, **more_nums}
print(f"Merged: {all_nums}")

# Keys and values
print(f"Keys: {list(all_nums.keys())}")
print(f"Values: {list(all_nums.values())}")

# Sort
print(f"Sorted: {dict(sorted(all_nums.items()))}")

# Check
print(f"Has 'five'? {'five' in all_nums}")