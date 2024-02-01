nums=[1,3,4,8,7,9,3,5,1]
n=len(nums)
if n %3 !=0:
    print("array len is less than 3")

nums.sort()

result = []
        #group_index = 0
for i in range(0, n, 3):
    if i + 2 < n  and nums[i + 2] - nums[i] <= 2:
        result.append([nums[i], nums[i + 1], nums[i + 2]])
        print(result)
                #group_index += 1
    else:
        print("empty array")

        


    