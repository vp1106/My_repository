# Lab Class-27-FEB'

# 1. Write Python functions to perform the following operations:

# a) Find the square of a number.
# b) Check whether a number is even or odd.
# c) Return the maximum of three numbers.
# d) Find the sum of elements in a list.

def FindSquare(num):
    result = (num)**2
    return result

def CheckEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def MaxOfThree(x=0, y=0, z=0):
    return x if (x > y and x > z) else (y if y > z else z)

def SumOfElements(mylist=[], mysum=0):
    mysum += sum(x for x in mylist)  # Fixed: use sum() function
    return mysum


ans=FindSquare(25)
print(ans)
ans=CheckEven(25)
print(ans)
ans=MaxOfThree(23,56,1)
print(ans)
ans=SumOfElements([12,22,33,13,71])
print(ans)

