import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


API_TOKEN = "8285316926:AAEwRSMsbmmx29XkgzlUWBnoD_e44lIVbBo"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

games = {}


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}! 👋\n" "i'm a random number Telegram-Bot\n")

@dp.message(Command("random"))
async def start_game(message: types.Message):
    number = random.randint(1, 100)
    games[message.from_user.id] = {
        "number": number,
        "attempts": 0,
        "max_attempts": 10
    }
    await message.answer("Я загадал число от 1 до 100. Попробуй угадать!")

@dp.message()
async def guess_number(message: types.Message):
    user_id = message.from_user.id
    if user_id not in games:
        await message.answer("Сначала начни игру командой /random ")    
        return

    game = games[user_id] 

    try:
        guess = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введи число!")
        return

    game["attempts"] += 1

    if guess < game["number"]:
        await message.answer("Моё число больше ")
    elif guess > game["number"]:
        await message.answer("Моё число меньше")
    else:
        await message.answer(f"Поздравляю! Ты угадал число {game['number']} за {game['attempts']} попыток 🎉")
        del games[user_id]
        return

    if game["attempts"] >= game["max_attempts"]:
        await message.answer(f"Ты проиграл  Загаданное число было {game['number']}.")
        del games[user_id]

    
        
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

