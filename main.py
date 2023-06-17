import os
import asyncio
import logging

from aiogram import Bot, Dispatcher

from utils.commands import set_commands

from handlers import start, before_contest, user_info


async def main() -> None:
    bot = Bot(token=os.getenv("token"))
    dp = Dispatcher()

    dp.include_routers(start.router, before_contest.router, user_info.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
