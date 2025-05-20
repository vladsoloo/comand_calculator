import asyncio
import os
from loguru import logger
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher
<<<<<<< HEAD
from aiogram.client.default import DefaultBotProperties
from chat import numbers
=======

dp = Dispatcher()
>>>>>>> 6be7e7188a4daa8b848032f9e80e13b30a8603d0

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")


<<<<<<< HEAD
async def main1():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
=======
async def main() -> None:
    logger.add('file.log',
               format='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}',
               rotation='3 days',
>>>>>>> 6be7e7188a4daa8b848032f9e80e13b30a8603d0
               backtrace=True,
               diagnose=True)
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Бот остановлен")

<<<<<<< HEAD
    numbers(dp)


if __name__ == '__main1__':
    asyncio.run(main1())
=======
if __name__ == "__main__":
    logger.info('Бот запущен')
    asyncio.run(main())
>>>>>>> 6be7e7188a4daa8b848032f9e80e13b30a8603d0
