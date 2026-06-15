# 05 MARCH THURSDAY-CLASSES intricacies

#class inheritence

# class Base:
#     def __init__(self,name) :
#         self.name=name
#         print("inside base class constructor")
        
#     def printbase(self):
#         print(self.name,"from the base class")
#         #print(self.rollno,"roll no from the base class")#derived obj has no attribute roll no
        
        
# class Derived(Base):#note that u have the base class as a parameter for the derived class
#     def __init__(self,rollno,name):
#         super().__init__(name) # note the syntax super().__init__(parameters)
        
#         # do if i have two base classes with same parameters which one would the function choose?
        
#         self.roll=rollno
#         print("inside the derived class constructor")
#     def printderived(self):
#         print(self.roll,"roll no from derived class")
#         print(self.name,"name from base class")#will that work??
        
# o1=Derived(55,"veda")
# o1.printderived()
# o1.printbase()

# o2=Base("name")
# o2.printbase()
        
#Multi         