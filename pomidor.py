import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import find_dotenv, load_dotenv
from loguru import logger

# Настройка Loguru
logger.add("spy_bot.log", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO")

# Загрузка конфига
load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))  # Ваш ID в Telegram

bot = Bot(token=TOKEN)
dp = Dispatcher()

# При любом сообщении бот логирует данные и шлет их админу
@dp.message()
async def spy_on_user(message: Message):
    user = message.from_user
    user_data = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "text": message.text
    }

    # Логируем в терминал
    logger.info(f"Данные пользователя: {user_data}")

    # Шлем админу в ЛС
    await bot.send_message(
        ADMIN_ID,
        f"🔍 Новые данные:\n"
        f"ID: {user.id}\n"
        f"Имя: {user.first_name}\n"
        f"Фамилия: {user.last_name}\n"
        f"Username: @{user.username}\n"
        f"Сообщение: {message.text}"
    )
