# 


 # Given two matrices A and B (list of lists) perform the following operations using zip() and *(unpacking) operator.


 #    (a) Interchange any two rows

 #    (b) Interchange any two columns 

 #   You can take suitable inputs for rows / columns

# Matrix operations with zip and *

def show(m, t):
    print(f"\n{t}:")
    for r in m: print(r)

def row_swap(m, a, b):
    m = [r[:] for r in m]
    m[a], m[b] = m[b], m[a]
    return m

def col_swap(m, a, b):
    t = list(zip(*m))
    t[a], t[b] = t[b], t[a]
    return [list(r) for r in zip(*t)]

# Test
A = [[1,2,3],[4,5,6],[7,8,9]]
show(A, "Original")

r = row_swap(A, 0, 2)
show(r, "Rows 0 and 2 swapped")

c = col_swap(A, 0, 2)
show(c, "Cols 0 and 2 swapped")

# Get user input
r = int(input("Rows: "))
c = int(input("Cols: "))
m = [[int(input(f"[{i}][{j}]: ")) for j in range(c)] for i in range(r)]

show(m, "Your matrix")
op = input("Swap (r)ows or (c)olumns? ")

if op == 'r':
    a,b = int(input("Row1: ")), int(input("Row2: "))
    show(row_swap(m, a, b), "Result")
else:
    a,b = int(input("Col1: ")), int(input("Col2: "))
    show(col_swap(m, a, b), "Result")