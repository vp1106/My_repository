#11 feb Lists-cont


# lst=[10,30,20,30,50,60]
# lst.remove(30)# removes the first 30
# lst.append(25)
# lst.pop()#removes from the end by default
# lst.pop(2)
# print(lst)


# # sorted() returns a new sorted list and leaves the original unchanged.
# # .sort() sorts the list in-place and returns None.


# lst2=[10,22,45,6]
# lst2.sort()
# print(lst2)
# lst3=sorted(lst2)

# print(lst3)


#shallow copy and deep copy

# list1=[22,34,56,"random"]
# copylist=list1.copy()
# copylist[1]="new"
# print(copylist)#copy appended
# print(list1)#org remains unchanged
# copylist.append([5,6])
# print(copylist)
# print(list1)# again orginal not changed





# CW: 1) Define two lists of strings. Use relational operators to 
# compare them.  What can you say? 
# 2) Instead of both lists as strings, change one of them to integers 
# and then use relational operators. What can you say?

mylist1=["random","list"]
mylist2=["of","strings"]

# mylist1.sort()
# mylist2.sort()
# newlist=mylist1+mylist2
# newlist.sort(key=len)
# print(newlist)

#sorted alphabetically if sort() normally
#key=len sort by length

list1=["veda",22,33,5]
print(*list1)
llist=[[12,333],[22,34]]
print(*llist)
#unpacking operator-sqr bracket removed-elements
# for list of list unpacking op removes only the outer bracket

#print all items individually even if list of list
for ele in llist:
    if type(ele).__name__=="list":
        for i in ele:
            print(i)
    else:
        print(i)
        
#any other way?-list comprehension

flattened=[item for sublist in llist for item in sublist]
for i in flattened:
    print(i)
 
import random
lst1=[random.randint(10,100) for n in range (12)]#12 random integers btw 10,100 noice
print(lst1)




