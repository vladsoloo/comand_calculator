import asyncio
import os
from loguru import logger
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from chat import run_bot

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

def main0():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")

    while True:
        try:

            num1 = float(input("Введите первое число: "))
            operator = input("Введите оператор (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Ошибка: Деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Ошибка: Неверный оператор!")
                continue

            again = input("Хотите выполнить еще одно вычисление? (да/нет): ")
            if again.lower() != 'да':
                print("Спасибо за использование калькулятора!")
                break

        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число!")
            continue


if __name__ == 'main0':
    main0()

async def main1():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    logger.info("Бот запущен")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Бот остановлен")

    run_bot()


if __name__ == '__main1__':
    asyncio.run(main1())
