numbers = [4, 7, 2, 9, 12, 5, 3, 10]
GreaterFive = []
for i in numbers:
    if i > 5:
        GreaterFive.append(i)
min_value = GreaterFive[0]
max_value = GreaterFive[1]
for x in GreaterFive:
    if x < min_value:
        min_value = x
    if x > max_value:
        max_value = x
print(min_value)
print(max_value)  
print(GreaterFive)
