nums = [5]
k = 9
l=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        #print(nums[i:j])
        if sum(nums[i:j])%k==0:
            l.append(nums[i:j])

print(len(l))
            