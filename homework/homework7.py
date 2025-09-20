a = 1
b = 1
n = int(input("введите число"))
if  0 < n < 47:  
    for fn in range (2,n):
        a, b = b, a + b
print(b)