# 23 FEB-CLASSWORK

#come up with a function with the order of pos and  keyword arguments

# def diffunction(x=0,y=0):#default arg
#     mydiff=x-y
#     return(mydiff)

# mysum=diffunction(3,6)
# mysum1=diffunction(y=23,x=3)
# mydef=diffunction()
# print(mysum1)
# print(mysum)
# print(mydef)

# #recursion
# def print_num(num):
#     if num>0:
#         print_num(num-1)
#         print(num)
 
# def print_num(num):
#         if num>0:
#             print(num)
#             print_num(num-1)
# print_num(10)

#factorial
def factorial(n):
    if n<1:
        return 1
    else:
        return(n*factorial(n-1))
    
ans=factorial(5)
print(ans)
        
def Sumofdigits(num):
    if num==0:
        return 0
    else:
        return(num%10)+Sumofdigits(num//10)#% is remainder // qt
Ans=Sumofdigits(123)
print(Ans)
        
avg=lambda a,b:(a+b)/2
print(avg(22,33))

#map function-return map object
