def make_unique(nums):
    nums.sort()  # Sort the list first
    n = len(nums)
    increments = 0  # Track the total increments

    for i in range(1, n):
        # If current element is not greater than the previous, increment it to be unique
        if nums[i] <= nums[i - 1]:
            new_value = nums[i - 1] + 1
            increments += new_value - nums[i]
            nums[i] = new_value

    return increments

# Test the function with the given list
nums = [3, 2, 1, 2, 1, 7]
print(make_unique(nums)) 