temp=['73','74','75','71','69','72','76','73']
res=[0]*len(temp)
ans=[]
for t in range(0,len(temp)):
    
    
    for s in range(t+1,len(temp)):
        if temp[t]<temp[s]:
            res[t]=s-t
            break
print(res)
