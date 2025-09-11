nums = [4, 7, 2, 7, 3, 4, 9, 9, 1]
maxInt = max(nums)
minInt = min(nums)
maxIndex = nums.index(maxInt)
minIndex = nums.index(minInt)
nums[maxIndex],nums[minIndex]=nums[minIndex],nums[maxIndex]
print (nums)