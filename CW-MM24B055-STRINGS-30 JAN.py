# class work 30 jan-friday
a=5 
print(id(a))
a=10
print(id(a))
b=10
print(id(b))
#b and a have same memmory location -so will changing b change a?
x = 5
print(id(x))  # Memory address, e.g., 140736123456

x = x + 1     # "Modifying" x
print(id(x))  # NEW memory address! Different object
print(x)      # 6

#integers are also immutable in python
#it makes a new integer and reassigns to that variable

text = "heLlo"

# Check type
print(type(text))  # <class 'str'>

# Check object ID
print(id(text))    # e.g., 1402456789012

# Call string methods
# print(text.upper())   # "HELLO"-uppercase
# print(text.isalpha()) # True-checks if all char are alphanumeric
# print(text.swapcase())#swaps lower to upper and vice versa
# print(text.encode())
# print(type(text.encode()))# what does encode do -what is type 'bytes'
# print(text.capitalize())# just the first letter capitalized
# print(text.find("e"))#find pos

print(text.find("l"))# reports the last instance not the first instance
print(text.replace("l","w"))# all instances replaced

str1="hell0 world"
print(str1.rfind("o"))
print(str1.split())
# See available methods
#print(dir(text))      # Lists all string methods

#WAP -write a program

str1="veda!!!v"
print(len(str1))#starts from 1

print(str1.rstrip("!"))#removes the specified characters
print(str1.rstrip("v"))#characters not removed?-ctrailing char removed

#input methods

# a=input("enter number 1")
# b=input("enter number 2")
a,b=input("enter num 1 and 2").split("-")#default is taken as space seperator else mention the seperator
print(a)
print(b)
#u have only identifier will it take multiple inputs

# print(type(a))
# c=a+b
# print(c)# concatenated as string

#use int input to take input as int()
text="hello-world-python"
result = text.partition("-")
print(result)  # ('Hello', '-', 'World-Python')
print(type(result))  # <class 'tuple'>

#seperator-default-space
print(a, b,sep='+', end='\n\n')


