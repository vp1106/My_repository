#TUPLES
tup=()
print (tup)

#built in tuple func
mytuple=tuple()

li = [1, 2, 4, 5, 6]
print(tuple(li))

#tuple of string float list tuple

# CW: Define a tuple of different datatypes and print 
# them using iterator. 
# HW:In a tuple, find the number of objects of each type.

mixtuple=("veda","knowledge",11,2006,(1,2,3),["a","b","c"])
countint=0
countstr=0
countlist=0
counttuple=0
for ele in mixtuple:
    print(f"the element {ele} is of the type:",type(ele).__name__)
    if type(ele).__name__=="str":
        countstr+=1
    elif type(ele).__name__=="int":
        countint+=1
    elif type(ele).__name__=="tuple":
        counttuple+=1
    elif type(ele).__name__=="list" :
              countlist+=1
    else:
        "element is not of str int tuple or list"
print(countint,countlist,countstr,counttuple)

        
    

    