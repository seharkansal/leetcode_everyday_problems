def majority_element(nums):
    n=len(nums)
    maxcount = 0; 
    element_having_max_freq = 0; 
    for i in range(0, n): 
        count = 0
        for j in range(0, n): 
            if(nums[i] == nums[j]): 
                count += 1
            if(count > maxcount): 
                maxcount = count 
                element_having_max_freq = nums[i] 
    
    return element_having_max_freq

nums=[10,20,40,40,40,10]
print(majority_element(nums))