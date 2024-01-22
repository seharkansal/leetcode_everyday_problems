num_set=[2,2]
dup=[]
for i in range(1,len(num_set)+1):
    total_num=num_set.count(i)
    if total_num==2:
        dup.append(i)
    if total_num==0:
        dup.append(i)

print(dup)
