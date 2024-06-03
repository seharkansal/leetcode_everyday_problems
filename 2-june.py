p="hello"
l=[]
for i in p:
    ans=ord(i)
    l.append(ans)
sum=0
for i in range(0,len(l)-1):
        diff=abs(l[i]-l[i+1])
        sum=sum+diff
print(sum)