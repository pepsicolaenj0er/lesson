import re

passwords = [
    "qwerty",
    "Password123",
    "admin",
    "HelloWorld!",
    "Qwe123!@#",
]

rules = [
    (lambda s: len(s) >= 8, "меньше 8 символов"),
    (lambda s: re.search(r"[A-Z]", s), "нет заглавной буквы"),
    (lambda s: re.search(r"[0-9]", s), "нет цифры"),
    (lambda s: re.search(r"[!@#$%^&*]", s), "нет спецсимвола"),
]

for password in passwords:
    errors = [msg for rule, msg in rules if not rule(password)]
    if errors:
        print(password, "→ слабый (" + ", ".join(errors) + ")")
    else:
        print(password, "→ надёжный")
