trust=[[1,3],[2,3]]
n=3
out_deg=[0]*(n+1)
in_deg=[0]*(n+1)
print(in_deg)
for a in trust:
    out_deg[a[0]]+=1
    in_deg[a[1]]+=1
print(out_deg)
print(in_deg)
for i in range(0,n+1):
    if out_deg[i]==0 and in_deg[i]==n-1:
        print(i)


