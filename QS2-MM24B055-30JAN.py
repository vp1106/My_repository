# In the class, we saw different approaches to solve the largest (or smallest) of three numbers. 

a,b ,c  = map(int, input("Enter three numbers separated by a space: ").split())#map func

# #in nbuilt max and min

print("max is",max(x,y,z))
print("min is",min(x,y,z))

#array func
array = [x, y, z]
array.sort()
largest  = array[2]
smallest = array[0]

print(largest)
print(smallest)


# b part

max_val = a if a >= b and a >= c else (b if b >= c else c)
min_val = a if a<=b and a<=c else(b if b<=c else c)
print("max val",max_val,"min val",min_val)


if x>=y and z:
    print("max is",x)
elif y>=x and y>=z:
    print("max is",y)
else:
    print("max is",z)

if x<=y and z:
    print("min is",x)
elif y<=x and y<=z:
    print("min is",y)
else:
    print("min is",z)