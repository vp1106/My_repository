# #List cotainer
# #A list is a container that can hold multiple items (of same or different type),they
# #are MUTABLE


# fruits = ["tomato","apple", "banana", "cherry"]
# fruits.sort()#sort works if all are same data type
# fruits.append(3.14)
# print(fruits)
# numbers = [1, 2, 0, 4, 5]
# numbers.sort()
# print(numbers)
# mixed = [10, "hello", 3.14]
# #mixed.sort()
# print(mixed)
# print(mixed[0])
# print(mixed[-1])

# fruits.append("cherry")#append takes one argument only
# #can have duplicate values
# print(fruits)
# #fruits.insert("jackfruit","tomato")#insert takes integer arg only


# # list methods
# lst = [10, 20]
# lst.append(30)      # [10, 20, 30]
# lst.insert(2,15)   # [10, 20, 15, 30]
# lst.sort()
# #insert(the index to insert,the value to insert)
# print(lst)
# lst.remove(30)
# print(lst)
# lst.reverse()
# print(lst)
# print(sum(lst))
# print(len(lst))

# #check type befor sorting?
# for item in [10, "hello", 3.14, [1, 2]]:
#     print(f"{item} is type: {type(item)}")#learn f string {item}
# #you can have list within list

# #how to check data type and then sort?


# #cw define a list of strings and find and print the number of characters in each of them

# mylist=["veda","baby","happy","random"]
# for ele in mylist:
#     print(f"number of characters in {ele} is : ",len(ele))

# # list op
    
# #conactenation
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = list1 + list2  # [1, 2, 3, 4, 5, 6]
# print(result)

# #repetition

# list1 = [1, 2]
# repeated = list1 * 3  # [1, 2, 1, 2, 1, 2]

# #membership
# fruits = ["apple", "banana", "cherry"]
# print("apple" in fruits)   # True
# print("grape" in fruits)   # False

# numbers = [10, 20, 30, 40, 50]

# print(len(numbers))   # 5
# print(sum(numbers))   # 150
# print(min(numbers))   # 10
# print(max(numbers))   # 50

# nums = [3, 1, 4, 1, 5, 9]

# # Creates new sorted list
# sorted_nums = sorted(nums)        # [1, 1, 3, 4, 5, 9]
# sorted_desc = sorted(nums, reverse=True)  # [9, 5, 4, 3, 1, 1]

# # Sorts in-place (modifies original)
# nums.sort()           # nums becomes [1, 1, 3, 4, 5, 9]
# nums.sort(reverse=True)  # [9, 5, 4, 3, 1, 1]

# nums = [3, 1, 4, 1, 5, 9]

# # Creates new sorted list
# sorted_nums = sorted(nums)        # [1, 1, 3, 4, 5, 9]
# sorted_desc = sorted(nums, reverse=True)  # [9, 5, 4, 3, 1, 1]

# # Sorts in-place (modifies original)
# nums.sort()           # nums becomes [1, 1, 3, 4, 5, 9]
# nums.sort(reverse=True)  # [9, 5, 4, 3, 1, 1]#reverse=True for descending order

# #custom sort based on length of word

# words = ["apple", "banana", "kiwi", "grape"]

# words.sort()
# print(words)
# # Sort by length (shortest to longest)
# words.sort(key=len)
# print(words)  # ['kiwi', 'apple', 'grape', 'banana']

# # Sort by length (longest to shortest)
# words.sort(key=len, reverse=True)
# print(words)  # ['banana', 'apple', 'grape', 'kiwi']

# letters = ['a', 'b', 'c', 'd', 'e', 'f']

# print(letters[0])     # 'a' (first)
# print(letters[-1])    # 'f' (last)
# print(letters[1:4])   # ['b', 'c', 'd'] (slice 1 to 3)
# print(letters[:3])    # ['a', 'b', 'c'] (first 3)
# print(letters[3:])    # ['d', 'e', 'f'] (from index 3)
# print(letters[::2])   # ['a', 'c', 'e'] (every 2nd)
# print(letters[::-1])  # ['f', 'e', 'd', 'c', 'b', 'a'] (reverse)
# print(letters[::-2])  # ['f','d','b'] (reverse)
# letters.clear()
# print(letters)


#  #list i other lists

# nested = [[1, 2], ["a", "b"], [True, False]]
# print(nested[0][1])  # Output: 
    
# #09 feb
# #strings are immutable-sequence-can be run thru a loop
# #range is also a seq
# #while and for loop-while req cond-for req a seq

#print an id card

# Name,RollNo,Pincode=input("please enter the name,rollno,pincode seperated by -").split("-")
# print(Name)
# print(RollNo)
# print(Pincode)

# class ID_card:
#     def __init__(self,name,age,rollno,pincode):
#         self.Name=name
#         self.age=age
#         self.Pincode=Pincode
#         self.rollno=rollno
#     def printfunc(self):
#         print()

        # print the list
# mylist=["veda",'random',23,[2,3],{1,2,3},78,"lucky"]
# vlist=[11,23,45,3,23]
# del vlist[::2]#except the last two

# mylist.remove('random')
# mylist.pop()
# del mylist[2]
# del mylist[1:4]
# mylist.sort()
# print(vlist.sort())
# print(vlist)
# vlist2=sorted(vlist)
# print(vlist2)
# #needs to be of same data type

# #for list in list or a set

# # for ele in mylist:
# #     if type(ele).__name__=="list" or type(ele).__name__=="set":
# #         for i in ele:
# #             print(i)
# #     else:
# #         print(ele)
        
# for ele in mylist:
#     print(ele)

# print(len(mylist))
#will  not count the list within list or set within list
#try coding numberof indiv elemmnts if it is a list within list

#type func just object but you need a data type
# for ele in mylist:
#     print("the data type of the element",ele,"is",type(ele).__name__)#dont want it as a class int just as that data type
  
# #CW: Define a list of marks for a student and find the 
# max, min and average of them. Arranged the in sorted 
# order. Print all of them clearly. Delete the entire list and 
# check for emptiness. 

marks=[23,34,67,89,14,99,100,56,78,76,77,67,56,34]
if marks:
    print("not empty")
print ("max is ,",max(marks))
print ("min is ,",min(marks))
print ("avg is ,",sum(marks)//len(marks))
print("sorted array")
marks.sort()
print(marks)
marks.clear() #del just deletes the entire list while clear just removes the items
print(marks)

