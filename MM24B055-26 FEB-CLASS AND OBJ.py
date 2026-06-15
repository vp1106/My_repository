#Classes And Objects-26TH FEB
    
#NO Classes amd Variables in C-C uses structuresm instead!!!-Fake methods and Pseudo objects

#classes help us define objects and their methods-data is acessed thru them
#oops concepts-methods accessed thru object instaniation

# class StudentDetails:
    
#     def DataInput(self,n,r,s):
#         self.name=n
#         self.rollno=r
#         self.sem=s
    
#     def PrintOut(self):
#         print(self.name,self.rollno,self.sem,sep="\n")#note the seperator operator
        
# s1=StudentDetails()#object instantaition 
# s1.DataInput("Ram", 12, 3)
# s1.PrintOut()

# #use constructor
# class StudentDetails:
    
#     def __init__(self,n="",r=1,s=1):#constructor-give def value?
#         self.name=n
#         self.rollno=r
#         self.sem=s
    
#     def PrintOut(self):
#         print(self.name,self.rollno,self.sem,sep="\n")#note the seperator operator
        
# s1=StudentDetails("Ram",12,3)#object instantaition 
# s2=StudentDetails()
# s2.PrintOut()
# s1.PrintOut()

# # #Public data
# class StudentDetails:
    
#     def DataInput(self,n,r,s):
#         self.name=n
#         self.rollno=r
#         self.sem=s

        
# s1=StudentDetails()#object instantaition 
# s1.DataInput("Ram", 12, 3)
# print("name =",s1.name,"roll no =",s1.rollno,"sem =",s1.sem)#all data is public now

# #Private Data
# class StudentDetails:
    
#     def DataInput(self,n,r,s):
#         self._name=n
#         self.__rollno=r
#         self.__sem=s
    
        
# s1=StudentDetails()#object instantaition 
# s1.DataInput("Ram", 12, 3)
# print("name=",s1._name)#protected not private-underscore and dunderscore
# print("rollno",s1.__rollno)#attributerror-private?

# #notionally private
# #strictly private


# # #name-accessible anywher/_name-protected/__name-Private

# #Destructor?

# class StudentDetail:
#     #Constructor
#     def __init__(self, n='R', r=1, s=1):
#         self._name = n
#         self._rollno = r
#         self._sem = s
# #Printing the data
#     def printout(self):
#         print('name = ', self._name, ", " , 'roll no = ',  self._rollno, ", " , 'sem = ', self._sem)
#     #destructor
#     def  __del__(self):
#         print('Del obj' + str(self))
# s1 = StudentDetail()
# s1.printout()
# s1 = StudentDetail('Ram')
# s1.printout()
# s1 = StudentDetail('Raman', 23)
# s1.printout()
# s1 = StudentDetail('Ramana', 23, 5)
# s1.printout()

# #__del__ intiated only when objects reference count hits zero?-when there is an instance still running -del ownt run//

# #class variable
# import math

# class CMV:
#     count = 0
    
#     def __init__(self, n = '', s = 0, c = ''):
#         self._name = n
#         self._size = s
#         self._color = c
#         CMV.count += 1
    
#     def display():
#         print(CMV.count)
        
# c1 = CMV('R', 1, 'B')
# print(CMV.count) 
# c2 = CMV('R', 1, 'B')
# print(CMV.count) 
# CMV.display()

# print(vars(CMV))  #dictionary of attributes
# print()
# print(dir(CMV))   #list of attributes

# print(vars(math))
# print()
# print(dir(math))

#Class Attribute;-master variable common to all objects like CMV.count
#Static Method-display method doesnt use self-use CMV.display() c1.display() will not work//
#similar to static members in C


#decorator-?-later

# def fun():
#     print('Inside fun')

# class Example:
#     def __init__(self, n='', r=''):
#         self._name = n
#         self.__roll = r
        
#     def print_details(self):
#         print(self._name, self.__roll)
        
#     def show():#static method
#         print('Inside show: class method')
#         fun()
        
# e1 = Example()
# e2 = Example('Ram','2345')
# e1._name = 'Ramana'#protected
# e1.__roll = '1234'#private
# e1.print_details()
# e2.print_details()

# Example.show()#static method-no self


#operator overloading

class Complex:
    def __init__(self, r=0, im=0):
        self._real = r#default arguments
        self._imag = im#default argumnets
        print(self)
        
    #Addition of two complex numbers using a method
    def add_comp(self, other):
        c = Complex()
        c._real = self._real + other._real
        c._imag = self._imag + other._imag
        return c#ensure to return or will throw an error
    
    #Addition of two complex numbers using operator overloading
    def __add__(self, other):
        c = Complex()
        c._real = self._real + other._real
        c._imag = self._imag + other._imag
        return c
    
    def __sub__(self,other):
        
        c = Complex()
        c._real = self._real - other._real
        c._imag = self._imag - other._imag
        return c
    
    def __mul__(self,other):
        c=Complex()
        c._real=(self._real*other._real)+(self._imag*other._imag)
        c._imag=(self._imag*other._real)+(self._real*other._imag)
        return c
    def print_comp(self):
        
        print('real = ', round(self._real,2), 'imag = ',round( self._imag,2))
        
    def Find_mag(self):
        mag=round(((self._real)**2+(self._imag)**2)**0.5,2)
        print(mag)
        
        
c1 = Complex(4.5, 5.45)
c2 = Complex(3.5, 8.45)
# c1.Find_mag()
c5=c1*c2

c5.print_comp()
# c3 = Complex()
# c4=Complex()
# #c3.print_comp()
# c3 = c1.add_comp(c2)
# c1.print_comp()
# c2.print_comp()
# c3.print_comp()
# c4=c1-c2
# c3 = c1 + c2  #Using the symbol for addition
# # so  using this operator witht hese two objects calls for 
# #the__add__function -it hhas a print inside coz of which u c the mem add
# c3.print_comp()
# c4.print_comp()

# Operator,Magic Method,Action
# +,"__add__(self, other)",Addition
# -,"__sub__(self, other)",Subtraction
# *,"__mul__(self, other)",Multiplication
# /,"__truediv__(self, other)",Division
# //,"__floordiv__(self, other)",Integer Division
# %,"__mod__(self, other)",Modulo (Remainder)
# **,"__pow__(self, other)",Exponentiation (Power)

# Dynamic creation of attributes

# class Passbook:
#     pass

#     def printout(self):
#         print(self.name, self.num)
        
#     def printwithargs(*args):
#         for each in args:
#             print(each)
        
        
# p1 = Passbook()
# p1.name = 'Ram'
# p1.num = 12345
# p1.printout()
# print(p1.name, id(p1.name))

# p1.name='Raman'
# print(p1.name, id(p1.name))
# Passbook.printwithargs(p1.name, p1.num)
# p2 = Passbook()
# p2.name = 'Ram'
# p2.num = 12345
# p2.bal = 2345
# p2.printout()

# del p2.bal

# p2.printout()

# #p2 bal dynamic attr the rel ones are name and num



