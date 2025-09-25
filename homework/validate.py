import re

passwords = [
    "qwerty",
    "Password123",
    "admin",
    "HelloWorld!",
    "Qwe123!@#",
]

verifiedPassword = [] 
for password in passwords: 
    verifiedPassword.append(password)
    if not re.search(r"[A-Z]",password):          
        print("слабый")
    elif not re.search(r"[0-9]",password):          
        print("слабый")
    elif not re.search(r"[!@#$%^&*]",password):          
        print("слабый")
    elif len(password) < 8:
        print("слабый")
    else:
        print("надежный")



    

