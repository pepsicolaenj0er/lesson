nums = [4, 7, 2, 7, 3, 4, 9, 9, 1]
newNums = []
for i in nums: 
    if i not in newNums:
       newNums.append(i)

zxc = max(newNums)
cxz = [x for x in newNums if x != zxc]
secondZxc = max(cxz) 
print(newNums)
print(secondZxc)