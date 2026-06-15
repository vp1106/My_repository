# #Functions

# #lambda arguments: expression
# # Regular function
# def add(x, y):
#     return x + y

# # Lambda equivalent
# add_lambda = lambda x, y: x + y

# print(add_lambda(3, 5))  # Output: 8

# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # [1, 4, 9, 16]

# name=lambda:input("enter ur name")
# print(name)

# function

def Operations(x,y):
    s=(x+y)
    d=(x-y)
    return (s,d)

ans=Operations(5,3) #formal arguments #actual arguments
print(*ans)# return tuple then unpacking operator
