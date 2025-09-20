a = 1
b = 1
n = int(input("введите число"))
for n in range (2 , n):
    if  0 < n < 47:
        a, b = b, a + b
print(b)