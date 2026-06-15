# #  20 Feb Lab class

# #qs1

# int_tuple=(12,34,56,78,9,22)
# print("max is:",max(int_tuple),"\n","min is:",min(int_tuple))

# mylist=[]
# for i in range (len(int_tuple)-1,0,-1):
#     mylist.append(int_tuple[i])
    
# reversed_tuple=tuple(mylist)
# print(reversed_tuple)

# mytuple = (12, 34, 5, 78, 9)
# reversed_tuple = mytuple[::-1]
# print(reversed_tuple)  # Output: (22, 9, 78, 56, 34, 12)

# #merge two tuples and display results

# mytuple1=[12,33,45,"veda",5.43]
# mytuple2=[22,45,'random',3.45,101]
# newtuple=mytuple1+mytuple2
# print(newtuple)

# #print only even numbers from the tuple?
# # eventuple=(x for x in mytuple if x%2==0)#comprehension-tuple comprehension doesnt workk
# # print(eventuple)

# even_tuple=[x for x in mytuple if x%2==0]
# even_tuple=tuple(even_tuple)#converting list comp to tuple after that 
# print(even_tuple)

# mytuplenew=(22,"veda",5.45,13.7,-1)
# a,b,c,d,e=mytuplenew
# print(a,b,c,d,e)

# # If you need variable names dynamically
# my_tuple = (10, 20, 30, 40)
# var_names = ['a', 'b', 'c', 'd']

# # Create dictionary of variables
# variables = {name: value for name, value in zip(var_names, my_tuple)}#no clue about dictionaries-revise

# # Print all
# for name, value in variables.items():
#     print(f"{name} = {value}")
    
#3rd qs

#subset?
set1 = {1, 2, 3, 4, 5, 6}
set2 = {2, 4, 6}
set3={2,3,5,7,11}

# Check if set2 is a subset of set1
print(set2.issubset(set1))  # True
print(set1.issubset(set2))  # False

if (set1.intersection(set2)):
    print("not disjoint")
else: 
    print("disjoint")
    
print(set1)

# print(set1.clear())


#find  elements common to all three?
common=set1.intersection(set2).intersection(set3)
print(common)

sentence=input("enter the sentence with appropriate spaces")
words=[x for x in sentence.split()]
words=set(words)
print(*words)  

  