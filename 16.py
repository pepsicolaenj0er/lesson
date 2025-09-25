examples = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 8, -2, 10], 6)
]
def twoSum(nums,target):
    numberIndex = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in numberIndex:
            return[numberIndex[diff], i]
        numberIndex[num] = i

for nums, target in examples:
    print(f"nums = {nums}, target = {target} --> {twoSum(nums , target)}")