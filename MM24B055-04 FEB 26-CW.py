# 04/FEB/WEDNESDAY-5:00
 #relational operator
 
# print first 10 natural numbers

# i=1
# while i<11:
#     print(i,end=" ")
#     i+=1
    
# # print the string and its characters
# str1=input("pls enter the string")
# for i in str1:# containment check--in
#     print(i)
    
# i=0
# str1="veda"
# while i<len(str1):
#     print(i,str1[i])
#     i+=1
    
# for i in range(10):#0 to 9

#     print(i)

# for i in range(0,10,2):# step function
#     print(i)
    
# a=1
# while a:
#     print(a)
#     a+=1
#     if a>5:
#         break
    
# #check max of 3 numbers
# a,b,c=map(int,input("enter three numbers seperated by -:").split("-"))
# if a>=b and a>=c:
#     print("max is,",a)
# elif b>=c:
#     print("max is,",b)
# else:
#     print("max is,",c)
    
# #condensed form
# max_val= a if a>=b and a>=c else (b if b>=c else(c))
# print(max_val)    
    
#Print all unique combinations of 1, 2 and 3  
numbers = [1, 2, 3]

print("All unique combinations:")
# Singles
for i in numbers:
    print((i,))

# Pairs
for i in range(len(numbers)):
    for j in range(i , len(numbers)):
        print((numbers[i], numbers[j]))

# Triple
for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        for k in range(i,len(numbers)):
            print(numbers[i],numbers[j],numbers[k])
