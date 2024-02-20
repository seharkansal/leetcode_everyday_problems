l=[9,6,4,2,3,5,7,0,1]
l.sort()
n=len(l)
nums=range(0,n+1)
for element in list(nums):
    if element not in l:
        print(element)
