from aiogram import Bot, Dispatcher
from sqlalchemy.testing.provision import create_db
import asyncio
from MotivatorBot.handlers import admin_handlers, user_handlers
from MotivatorBot.db.session import create_db

from MotivatorBot.app.config import settings



bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

dp.include_router(admin_handlers.router)
dp.include_router(user_handlers.router)

# Запуск бота и подключение к базе данных
async def main():
	await create_db()
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())