#FRIDAY LAB CLASS- REVISION

#qs1
#Write a Python program to perform the following operations on tuples:

# a) Create a tuple of integers and find the maximum and minimum values in the tuple.

# b) Reverse a tuple without using any built-in reverse functions.

# c) Merge two tuples into a single tuple and display the result.

# d) Create a tuple of 5 numbers and print only the even numbers from the tuple.

# e) Unpack a tuple into separate variables and print each variable separately.

mytuple=(12,43,45,67,89,8)
print("maximum is",max(mytuple))
print("minimum is",min(mytuple))

rtuple=tuple(list(mytuple[::-1]))
print(rtuple)

mtuple=mytuple+rtuple

mytup=(11,22,33,44,55)
even_tuple=tuple(list([x for x in mytup if x%2==0 ]))
print("og tuple is",mytup)
print("even tuple is",even_tuple)


mytup = (10, 20, 30, 40, 50)

index = 0
while index < len(mytup):
    a = mytup[index]
    print(f"{a}")
    index += 1


