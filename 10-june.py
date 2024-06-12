heights = [1,1,4,2,1,3]
expected=sorted(heights)
count=0
for i in range(0,len(heights)):
    if heights[i]!=expected[i]:
        count+=1
print(count)
    