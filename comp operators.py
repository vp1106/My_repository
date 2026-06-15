# 02 FEB CLASS(2)
a,b,c=1,2,1
print(a,b,c)
print(a==b==c)
print(a<b<c)
print(a<b>c)
print(a!=b!=c)#slight hitch--
''' a != b != c is NOT equivalent to "all three are different"

It only checks that adjacent pairs are different: (a ≠ b) and (b ≠ c)

a and c could be equal!'''

