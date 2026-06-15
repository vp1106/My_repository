#Conditional statements and Loops

# if and else conditions


#0 is false
a = 0
if (a):
    print('Hello')
else:
    print('Given number is zero, hence hello is not printed as 0 is taken as FALSE')

def conditional(num):
    if (num > 0):
        return "Positive"
    else:
        return "Negative"
print(conditional(-23))

# Example 1: Simple arithmetic
print(0.1 + 0.2 == 0.3)  # False!
print(0.1 + 0.2)         # 0.30000000000000004

# Example 2: Repeated operations
result = 0.0
for i in range(10):
    result += 0.1
print(result == 1.0)  # False! (might be 0.9999999999999999)

# just == for comparison
## Using 2 else statements will give invalid syntax error
## The relational operator "==" might not work for floating point numbers
def compare_float_abs(a, b, tolerance=1e-9):
    return abs(a - b) <= tolerance

print(compare_float_abs(0.1 + 0.2, 0.3))  # True
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
print(math.isclose(1e-9, 0))         # False with default tolerance


from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  # True

#math.isclose()

x=23.56
if x==23.5:
    print("true")
else:
    print("false")
#check max of 3 numbers
a,b,c=map(int,input("enter three numbers seperated by -:").split("-"))
if a>=b and a>=c:
    print("max is,",a)
elif b>=c:
    print("max is,",b)
else:
    print("max is,",c)
    
#condensed form
max_val= a if a>=b and a>=c else (b if b>=c else(c))
print(max_val)    
    