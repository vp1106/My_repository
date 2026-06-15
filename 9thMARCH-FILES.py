# 9 TH MARCH MONDAY-FILES 

#File input and output

# Write / read text data

msg1 = 'This is message 1 \n'
msg2 = 'This is a course on Data Science \n'
msg3 = 'The course number is ED5340 \n'

f = open('messages.txt', 'w') #Opens a file for writing
f.write(msg1) #Writes a new string 
f.write(msg2)
f.write(msg3)
f.close() #Closes the opened file

f = open('messages.txt', 'r')  #Opens a file for reading
data = f.read() #Reads ALL lines into data
print(data)
print(type(data))
f.close()



