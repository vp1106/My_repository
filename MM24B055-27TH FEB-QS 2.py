# 2. Write Python functions to solve the following problems:

# a) Return the second largest element in a list.
# b) Remove duplicate elements from a list.
# c) Accept variable number of arguments (*args) and return their product.
# d) Accept keyword arguments (**kwargs) and display them properly.

def SecondLargest(mylist=[]):
    if len(mylist)<2:
        return
    mylist=mylist.sort()
    return(mylist[-2])

def RemoveDuplicates(mylist=[],duplicate=[]):
    for i in range(len(mylist)):
        if mylist[i]==mylist[i+1]:
            duplicate.append(mylist[i])
    return(mylist-duplicate)
    
def Product(*args):
    if not args:  # If no arguments passed
        return 1  # or return None based on requirement
    
    result = 1
    for num in args:
        result *= num
    return result


def DisplayKwargs(**kwargs):#double star
    if not kwargs:
        print("No keyword arguments provided")
        return
    
    print("Keyword arguments received:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Example
DisplayKwargs(name="John", age=25, city="New York", profession="Engineer")
# Output:
# Keyword arguments received:
#   name: John
#   age: 25
#   city: New York
#   profession: Engineer
# Example
print(Product(2, 3, 4))    # Output: 24
print(Product(5, 10, 2))   # Output: 100
print(Product())            # Output: 1)