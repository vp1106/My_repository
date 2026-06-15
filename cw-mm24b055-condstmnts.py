#```python
# if and else conditions

def conditional(num):
    if (num > 0):
        return "Positive"
    else:
        return "Negative"

## Using 2 else statements will give invalid syntax error
## The relational operator "==" might not work for floating point numbers

a, b = input('Enter both the numbers:',).split()

if (a > b):
    print(a, " is larger than ", b)
elif (a < b):
    print(b, " is larger than ", a)
else:
    print(a, " and ", b, " are equal")

## Largest out of three given numbers
a, b, c = input('Enter all the numbers:',).split()

if (a > b):
    if (a > c):
        print(a, " is the largest element")
    else:
        print(c, " is the largest element")
else:
    if (b > c):
        print(b, " is the largest element")
    else:
        print(c, " is the largest element")

## Smallest out of three given numbers
a, b, c = input('Enter all the numbers:',).split()

if (a < b):
    if (a < c):
        print(a, " is the smallest element")
    else:
        print(c, " is the smallest element")
else:
    if (b < c):
        print(b, " is the largest element")
    else:
        print(c, " is the largest element")

print(a != b != c)
print(a == b == c)

a = -1
if (a):
    print('Hello')
## This happens because any non-zero number is treated as TRUE

a = 0
if (a):
    print('Hello')
else:
    print('Given number is zero, hence hello is not printed as 0 is taken as FALSE')

help(min)