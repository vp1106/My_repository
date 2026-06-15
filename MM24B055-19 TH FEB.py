# #Dictionaries
# dct1={10:100,20:200,'ED1':'VEDA','ED2':'TARINI'}
# print(dct1)

# dct={}#empty dict not set

# for k in dct1.keys():
#     print(k,dct1[k])
    
# mylist=[34,24,43,11]
# mydict=dict.fromkeys(mylist,"value")
# print(mydict)

# studentdict={1:"student1",2:"student2",4:"student4",3:"student3",5:"student5"}
# newdict=sorted(studentdict)
# print(newdict)
# print(type(newdict))


# newdict.clear()
# if newdict:
#     print("not clear")
# else:
#     print("clear")
    
# newdict.update(studentdict)
# print(newdict)


studlist = {
    "Anand": {'DOB': '20/11/2001', 'Roll': 'ED1234'},
    "Ramesh": {'DOB': '19/11/2001', 'Roll': 'ED1235'},
    "Kamesh": {'DOB': '21/11/2001', 'Roll': 'ED1236'}
    
    
}

print(*studlist)#unpacking operator

for v in studlist.values():
    print(v['DOB'])
    
for k,v in studlist.items():
    print('DOB OF ', k, 'is',v['DOB'])
    
studlist.update()
# Output:
# 20/11/2001
# 19/11/2001
# 21/11/2001

