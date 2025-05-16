import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import find_dotenv, load_dotenv


def run_bot():
    # Настройка логгирования
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)

    # Загрузка токена из .env
    load_dotenv(find_dotenv())
    TOKEN = os.getenv("TOKEN")

    if not TOKEN:
        logger.error("Токен бота не найден! Проверьте файл .env")
        exit(1)

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Приветственное сообщение
    @dp.message(Command('start'))
    async def cmd_start(message: types.Message):
        try:
            user_name = message.from_user.first_name
            user_id = message.from_user.id
            logger.info(f"Пользователь {user_name} (ID: {user_id}) запустил бота")

            welcome_text = (
                f"🔢 Привет, {user_name}! Я — бот-калькулятор. 🧮\n\n"
                "Просто напиши мне математическое выражение (например, '2+2', '5*3' или '10/2'), "
                "и я мгновенно решу его! 😊\n\n"
            )
            await message.answer(welcome_text)
        except Exception as e:
            logger.error(f"Ошибка в команде start: {e}", exc_info=True)
            await message.answer("❌ Произошла ошибка при обработке команды")

    # Обработка математических выражений
    @dp.message()
    async def calculate(message: Message):
        try:
            user_id = message.from_user.id
            expression = message.text
            logger.info(f"Пользователь {user_id} отправил выражение: {expression}")

            expression = expression.replace("^", "**")  # Поддержка степеней
            result = eval(expression)  # Вычисление (опасно без валидации!)

            logger.info(f"Вычислено выражение: {expression} = {result}")
            await message.answer(f"✅ Результат: {result}")

        except ZeroDivisionError:
            logger.warning(f"Попытка деления на ноль: {expression} (пользователь {user_id})")
            await message.answer("❌ Ошибка: деление на ноль!")
        except Exception as e:
            logger.error(f"Ошибка вычисления: {expression} (пользователь {user_id}): {e}")
            await message.answer("❌ Ошибка: некорректный ввод. Пример: '2+2' или '5*3'")

    # Запуск бота
    logger.info("Бот запущен и готов к работе...")
    dp.run_polling(bot)


# Чтобы запустить бота при вызове скрипта
if __name__ == '__main__':
    run_bot()
