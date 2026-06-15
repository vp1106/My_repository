# qs1 WAP to check if a given number is a prime number.

Num=abs(int(input("enter a prime number")))
fl_list=[]
for i in range (2,Num):
    if Num%i==0:
        fl_list.append(i)
if fl_list==[]:
    print("Prime")
else:
    print("not prime")

