from fastapi import FastAPI
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print(generate_password())

app = FastAPI()

users = {}

@app.post("/register")
def register(username: str, password: str):
    if username in users:
        return {"error": "Пользователь уже существует"}

    users[username] = {
        "password": password,
        "failed_attempts": 0,
        "blocked": False
    }
    return {"message": f"Пользователь {username} успешно зарегистрирован"}


@app.post("/auth")
def auth(username: str, password: str):
    if username not in users:
        return {"error": "Пользователь не найден"}

    user = users[username]

    if user["blocked"]:
        return {"error": "Пользователь заблокирован. Сбросьте пароль через /reset"}

    if password != user["password"]:
        user["failed_attempts"] += 1
        if user["failed_attempts"] >= 3:
            user["blocked"] = True
            return {"error": "Аккаунт заблокирован после 3 неверных попыток."}
        return {"error": f"Неверный пароль. Осталось попыток: {3 - user['failed_attempts']}"}

    user["failed_attempts"] = 0
    return {"message": f"Добро пожаловать, {username}!"}


@app.post("/reset")
def reset(username: str, new_password: str):
    if username not in users:
        return {"error": "Пользователь не найден"}

    user = users[username]

    if not user["blocked"]:
        return {"message": "Ваш аккаунт не заблокирован. Смена пароля не требуется"}

    user["password"] = new_password
    user["failed_attempts"] = 0
    user["blocked"] = False

    return {"message": f"Пароль для {username} успешно изменён, аккаунт разблокирован."}

