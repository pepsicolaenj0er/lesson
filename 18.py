firstNumber = int(input("первое число"))
secondNumber = int(input("второе число"))
sign = input("+ - / *")
if sign == "+":
    print(firstNumber + secondNumber)
elif sign == "-" :
    print(firstNumber - secondNumber)
elif sign == "/" :
    print(firstNumber / secondNumber)
    if firstNumber == 0:
        print(firstNumber / secondNumber ,"деление на ноль невозможно")
else: 
    print(firstNumber * secondNumber)