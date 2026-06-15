# # sets in python

myset={1,2,3,3,45,67}
newset=set([23,451,2,"veda","random"])
help (set())
#print(myset[3])# no indexes#set obj not subscriptable

# #sets are unordered

# #can be used to remove duplicates
myset1=set((12,22,45,55,12,32))
print(myset1)


# # Integers hash to themselves, BUT...hash()
# # Sets use modulo arithmetic to decide where to store them

# #set(iterable)
#  #set of characters string?
# name="veda pramod"
# charset=set(name)
# print(charset)




# #using set orders itin a weird ass way?-memory and hashing

# for char in charset:
#     print(char,end="")
    
# mytuple=([12,33,45],4.5,67,"veda",67)#list is unhashable ad so cant be used in string?
# #both list and ttuples if nested cannot be hashed


# #myset2=set(mytuple)

# #set operations
# #sets are mutable..-though indexing not possible

# myset.add(69)
# #myset.update([22,34,5],"random",4.5)#update requires the arg to be iterable-even int wot work
# print(myset)  

# fset=frozenset("veda pramod")
# print(fset) 

# #cant add remove update frozenset

# #two sets cannot be concatenated?
# set1={12,22,34,34,56}
# set2={67,45,5,6,7,8}
# # set3=set1+set2
# print(set3)
#wont work obv
    
#memeber functions in set?

#The main difference is how they handle elements that don't exist in the set.remove()-if element isnt there raises error 
#discard() just does nothing

# exset={11,22,33,44,55}
# exset.remove(23)#will raise error
# exset.discard(23)#wont do shit
# print(exset)

#set methods

exset1={1,2,3,4}
exset2={22,33,1,4,67}

exset2.update(exset1)#update wants iterable arg
print(exset2)

print(exset2.issuperset(exset1))#use dot...
print(exset1.issuperset(exset1))#same thing tho

print(exset2.issubset(exset1))
print(exset2.issubset(exset2))

print(exset1.isdisjoint(exset2))

#symmetric difference/intersection/union
#Symmetric difference returns elements that are in either set, but not in both-A-B

#set comprehension
sqset={x**2 for x in range(1,10)}
print(sqset)

#updating set ops tricky -r3vise

import random

random1={ random.randint(1,100) for _ in range (12)}
random2={ random.randint(1,100) for _ in range (12)}

print(random1)
print(random2)


#random1|=random2 #union

random1&=random2 # intersection

random1^=random2#update symmetric difference

# random1-=random2

# random2-=random1

#print(random2)
print(random1)


