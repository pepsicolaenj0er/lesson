import random

secret = random.randint(1,100)
guess = None
attempts = 0 
maxAttempts = 10
while attempts <maxAttempts:
    guess = int(input ("предполагаемое число"))
    attempts += 1 

    if guess < secret:
        print ("больше")
    elif guess > secret:
        print ("меньше")
    else:
        print (attempts , "ты угадал")
        break 

else:
    print(secret , "ты проиграл")