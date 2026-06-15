# FEB 20 LAB CLASS
#QS2
#Create 3 tuples one for name, age and salary. Group them using indexing approach (with and without comprehension)
# and then with zip function. Print the output as a list.

name=("Anjali","Ram","Ghanashyam","Arjun")
age=(24,22,19,26)
salary=(120000,22000,22000,20000)

#group without comprehension:
# group=[]
# for i in range(len(name)):
#     group+=[(name[i],age[i],salary[i])]
# print(group)

#group with comprehension:
# group=[(name[i],age[i],salary[i]) for i in range(len(name))]
# print(group)

#group with zip
# group=[x for x in zip(name,age,salary)]
# print(group)

