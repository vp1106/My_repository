#QS6
#using continue
fl_list=[]
for i in range(8,501):
    if i%6==0 and i%7==0:
        fl_list.append(i)
    else:
        continue
    print(fl_list)

fl_list=[]
for i in range(8,501):
    if i%6==0 and i%7==0:
        fl_list.append(i)
    else:
        pass
    print(fl_list)