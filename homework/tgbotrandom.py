import asyncio
import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

games = {}

MESSAGES = {
    "start": "Привет, {name}! 👋\nЯ бот для игры в угадай число!",
    "no_game": "Сначала начни игру командой /random",
    "enter_number": "Пожалуйста, введи число!",
    "too_low": "Моё число больше 😉",
    "too_high": "Моё число меньше 😏",
    "win": "Поздравляю! Ты угадал число {number} за {attempts} попыток 🎉",
    "lose": "Ты проиграл 😢 Загаданное число было {number}.",
    "start_game": "Я загадал число от 1 до 100. Попробуй угадать!",
}


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(MESSAGES["start"].format(name=name))


@dp.message(Command("random"))
async def start_game(message: types.Message):
    number = random.randint(1, 100)
    games[message.from_user.id] = {
        "number": number,
        "attempts": 0,
        "max_attempts": 10
    }
    await message.answer(MESSAGES["start_game"])


@dp.message()
async def guess_number(message: types.Message):
    user_id = message.from_user.id
    if user_id not in games:
        await message.answer(MESSAGES["no_game"])
        return

    game = games[user_id]

    try:
        guess = int(message.text)
    except ValueError:
        await message.answer(MESSAGES["enter_number"])
        return

    game["attempts"] += 1

    if guess < game["number"]:
        await message.answer(MESSAGES["too_low"])
    elif guess > game["number"]:
        await message.answer(MESSAGES["too_high"])
    else:
        await message.answer(
            MESSAGES["win"].format(
                number=game["number"],
                attempts=game["attempts"]
            )
        )
        del games[user_id]
        return

    if game["attempts"] >= game["max_attempts"]:
        await message.answer(
            MESSAGES["lose"].format(number=game["number"])
        )
        del games[user_id]


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())