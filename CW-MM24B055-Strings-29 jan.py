#29 th JAN

#strings

#string representation

word1='veda'
word2="veda"
word3='''ve #multi line
da'''
print(word3)

str1 = 'Hello World'
str2 = 'It\'s raining'  # Escape needed for apostrophe(both single quotes)

print(str2)

str1 = "Hello World"
str2 = "It's raining"  # No escape needed for apostrophe-notice double quotes
str3 = "He said, \"Hello!\""  # Escape needed for quotes inside

print(str2)
print(str3)

#Multi-line strings
str1 = """This is
a multi-line
string"""

str2 = '''Another
multi-line
string'''

# Contains both single and double quotes without escaping
str3 = """It's "awesome"!"""

print(str1)
print(str2)
print(str3)

#raw strings-to avoid the escape

#raw string syntax---add r or R b4 quotes
# Regular string (escapes processed)
regular = "Hello\nWorld"

# Raw string (escapes ignored)
raw = r"Hello\nWorld"

print(regular)  # Hello (newline) World
print(raw)      # Hello\nWorld  ← literally shows \n


# accessing string elements-arrays
#as well as string slicing
str1="raman"
for i in range (-1,-6,-1):# should it be 5 or 6 :)) check!!
    print(str1[i])
print(str1[2])
print(str1[2:])#start included in genral-last one not included
print(str1[:-1])#everything until the last one
print(str1[-3:-1])# third from last to the second last

#includes first indice ignores last indice


#immuatable strings
text = "hello"
text=text[::-1]
print(text)

# ERROR: Can't change individual characters
#text[0] = "H"  # TypeError: 'str' object does not support item assignment

# Instead, create a new string:
#text = "H" + text[1:]  # Correct

#Captitalize/upper/lower

print(chr(25))#unicode?
print(ord("s"))

#chr fi rcharacter gives character for number in unicode and ord-ordinal-gives num for the character

#can be used for encryption decryption

# a=[(i,chr(i)) for i in range(97,123)]
# print(a)

# for i,item in enumerate(a):
#     print(f"Num:{i+97} character:{item}")#kakoii
 
# Name=input("enetr the name to be encoded")
# for i in Name:
#     if i==a[i]:
#         etxt+=a[chr(i)]

# encoded_map={chr(i):i for i in range(97,123)}
# Name=input("enter the name to be eencoded").lower()
# encoded_res=[]
# for char in Name:
#     if char in encoded_map:
#         new_code=encoded_map[char]+1
#         encoded_res.append(chr(new_code))
#     else:
#         encoded_res.append(char)#keep spaces as they are
# print(encoded_res.join())

# Sample Data
text = "  Python is Fun!      "
full_string = "apple-pie-recipe"

### 1. Global Functions (Independent)
# len(): Returns the count of items/characters
length = len(text) 

# str(): Converts any data type into a string
number_as_string = str(100) 

# chr(): Converts an integer (Unicode) to a character
char_val = chr(65) 

# ord(): Converts a single character to its integer Unicode value
ord_val = ord('A') 

### 2. String Methods (Called using .method())
# rstrip(): Removes whitespace (or specific chars) from the RIGHT side
clean_right = text.rstrip()

# index(): Finds the FIRST position of a substring (raises error if not found)
pos = text.index("is")

# partition(): Splits string into a 3-item tuple: (before, separator, after)
parts = full_string.partition("-")

# --- Displaying Results ---
print(f"1. len(): {length}")
print(f"2. str(): {type(number_as_string)} -> '{number_as_string}'")
print(f"3. chr(65): {char_val} | ord('A'): {ord_val}")
print(f"4. rstrip(): '{clean_right}' (Notice trailing spaces gone)")
print(f"5. index('is'): Found at index {pos}")
print(f"6. partition('-'): {parts}")


# Input: "1 2 3 4 5 6"
numbers = list(map(int, input("Enter all scores: ").split()))

print(f"Total items: {len(numbers)}")
print(f"Average: {sum(numbers)/len(numbers)}")

# The Code
nums = map(int, input().split())

# 1. User types: "5 10"
# 2. input().split() -> creates ["5", "10"]
# 3. map(int, ["5", "10"]) -> applies int("5") and int("10")
# 4. Result: (5, 10)