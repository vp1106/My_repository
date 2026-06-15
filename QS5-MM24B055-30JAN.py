# Given an integer or a string (assume to be a single word), find out the sum of its digits.

term=input("enter the term")
Nsum=0
if term.isdigit()==True:
    term=int(term)
    while term > 0:
        Nsum += term % 10  # extract last digit
        term //= 10 
    print(Nsum)
        
else:
    print("not a num ")
    
    
    
