# def recursion(n):
#     if n<=1:
#         return n
#     else:
#         return n+recursion(n-1)


# for i in range(10):
#     print("factorial of",i,"is",recursion(i))

def rec_pal(st,s,e):
    
    if st[s]!=st[e]:
        return False

    if s<e+1:
        return rec_pal(st,s+1,e-1)

    return True

def ispal(st):
    n=len(st)
    return rec_pal(st,0,n-1)

print(ispal('abab'))


    
