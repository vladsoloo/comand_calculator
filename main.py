import asyncio
import os
from loguru import logger
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher

dp = Dispatcher()
load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")


async def main1() -> None:
    logger.add('file.log',
               format='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}',
               rotation='3 days',
               backtrace=True,
               diagnose=True)
    bot = Bot(token=os.getenv('TOKEN'))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Бот остановлен")


if __name__ == '__main1__':
    asyncio.run(main1())
