# 5. Write Python programs to demonstrate basic class concepts:

# a) Create a class Student with attributes name and roll number.#
# b) Create an object of the class and print the attributes.#
# c) Add a method inside the class to display student details.#
# d) Create two objects and show that they store different data.#
# e) Print the type of the object created.#


class Student:
    
    def __init__(self,n="",r=0):
        self._name=n
        self._rollno=r 
        
    def DisplayStudentDetails(self):
        print("name is:",self._name,"roll no:",self._rollno)
        
#main\
s1=Student("Ramya",24)
print(s1._name,s1._rollno)
s1.DisplayStudentDetails()

s2=Student("Veda",55)
s3=Student("Rahul",36)
s2.DisplayStudentDetails()
s3.DisplayStudentDetails()
print(type(s1).__name__)
        
        