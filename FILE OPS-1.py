#  #Files I/O IN PYTHON-10 TH MARCH


# # Write / read text data

# msg1 = 'This is message 1 \n'
# msg2 = 'This is a course on Data Science \n'
# #msg3 = (ed5430) # always string not integer or any other data type?


# # f = open('messages.txt', 'w') #Opens a file for writing
# # f.write(msg1) #Writes a new string 
# # f.write(msg2)
# # #f.write(msg3)
# # f.close() #Closes the opened file

# # #file handle f and dont forget to close...

# # Name="veda"
# # subjects=" loves math\n" #newline here prolly
# # f=open('messages.txt','w')
# # f.write(Name)
# # f.write(subjects)
# # f.close()

# f=open('messages.txt','a')
# Name="Viba"
# subjects=" aced math"
# f.write(Name)
# f.write(subjects)
# f.close()

# # f = open('messages.txt', 'r')  #Opens a file for reading
# # data = f.read() #Reads ALL lines into data
# # print(data)
# # print(type(data))
# # f.close()

# with open('messages.txt', 'r+') as f:#automatically closes after code
#     f.write('Hello')
#     content = f.read()
#     print(content)
#     f.seek(0)  # Go back to beginning #seek to move pointer//
#     f.write("UPDATED: " + content)
  
# #Other write functions

# #msg4 = ['New\n', 'Course\n']
# msg4 = 'A new course\n'
# msg5 = ['New\n', 'Course\n']
# f = open('messages.txt', 'w')
# f.write(msg4)
# f.writelines(msg5)
# f.close()


# #Needs to be converted to strng before writing
# tup = ('Ram', 23, 1456)
# lst = [12, 23, 34]
# dct = {'Name' : 'Raman', 'Roll' : 123}
# tup1 = ('Ram1', 123, 14516)
# lst1 = [121, 213, 341]
# dct1 = {'Name1' : 'Raman1', 'Roll1' : 1123}
# f = open('messages.txt', 'w')
# f.write(str(tup))
# f.write(str(lst))
# f.write(str(dct))
# f.write('\n')
# f.write(str(tup1))
# f.write(str(lst1))
# f.write(str(dct1))
# f.close()



    
    

