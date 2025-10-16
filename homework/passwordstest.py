from fastapi import FastAPI
from pydantic import BaseModel
import random
import string
import bcrypt


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


app = FastAPI()


class UserCredentials(BaseModel):
    username: str
    password: str


users = {}


@app.post("/register")
def register(data: UserCredentials):
    username = data.username
    password = data.password

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    users[username] = {
        "password": hashed_pw,
        "failed_attempts": 0,
        "blocked": False
    }
    return {"status": "ok", "message": f"Пользователь {username} успешно зарегистрирован!"}


@app.post("/auth")
def auth(data: UserCredentials):
    username = data.username
    password = data.password

    if username not in users:
        return {"status": "error", "message": "Пользователь не найден"}

    user = users[username]

    if user["blocked"]:
        return {"status": "error", "message": "Пользователь заблокирован. Сбросьте пароль через /reset"}

    if not bcrypt.checkpw(password.encode(), user["password"].encode()):
        user["failed_attempts"] += 1
        if user["failed_attempts"] >= 3:
            user["blocked"] = True
            return {"status": "error", "message": "Аккаунт заблокирован после 3 неверных попыток"}
        return {"status": "error", "message": f"Неверный пароль. Осталось попыток: {3 - user['failed_attempts']}"}

    user["failed_attempts"] = 0
    return {"status": "ok", "message": f"Добро пожаловать, {username}!"}


@app.post("/reset")
def reset(data: UserCredentials):
    username = data.username

    if username not in users:
        return {"status": "error", "message": "Пользователь не найден"}

    user = users[username]

    if not user["blocked"]:
        return {"status": "error", "message": "Ваш аккаунт не заблокирован. Смена пароля не требуется"}

    new_password = generate_password()
    hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
    user["password"] = hashed
    user["failed_attempts"] = 0
    user["blocked"] = False

    return {
        "status": "ok",
        "message": f"Пароль для {username} успешно изменён, аккаунт разблокирован.",
        "new_password": new_password
    }


# В любом фастапе файле он будет запускаться за счет этой штуки))) затестить localhost:8000/docs в браузере 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
