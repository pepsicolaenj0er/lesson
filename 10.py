nums = [4, 7, 2, 7, 3, 4, 9, 9, 1]
even = 0
odd = 1
for i in nums:
    if i % 2 == 0:
        even += i 

for i in nums:
    if i % 2 != 0:
        odd *= i
print (odd)
print (even)