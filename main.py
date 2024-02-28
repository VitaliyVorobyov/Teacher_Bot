import asyncio
import logging

import asyncpg
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from core.utils.settings import settings
from core.utils.commands import set_commands
from core.middlewares.dbmiddleware import DbSession
from core.middlewares.validmiddleware import ValidationMiddleware
from core.utils.dbconnect import Request
from core.handlers import (basic, deletemessage, create_user_menu, help, statistics, add_content,
                           create_test, register)


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def create_pool(host: str, port: int, username: str, password: str, database_name: str):
    return await asyncpg.create_pool(
        user=username, password=password, database=database_name, host=host, port=port
    )


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s -"
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    storage: RedisStorage = RedisStorage.from_url(settings.redis.url)
    bot: Bot = Bot(token=settings.bots.bot_token)
    pool_connect: create_pool = await create_pool(
        host=settings.database.host,
        port=settings.database.port,
        username=settings.database.username,
        password=settings.database.password,
        database_name=settings.database.database_name)
    request: Request = Request(pool_connect)
    dp: Dispatcher = Dispatcher(storage=storage)
    dp.update.middleware.register(DbSession(pool_connect))
    # await request.create_table()
    dp.message.middleware.register(ValidationMiddleware([user['user_id'] for user in await request.get_users()]))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_routers(basic.router, create_user_menu.router, help.router, statistics.router, add_content.router,
                       create_test.router, register.router, deletemessage.router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f"[!!! Exception] - {ex}", exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
