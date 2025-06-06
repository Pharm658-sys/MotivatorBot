from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from MotivatorBot.db.crud import get_random_quote



router = Router()

@router.message(Command("start"))
async def cmd_users_start(message: Message):
	await message.answer("Добро пожаловать. Введите команду /random для получения рандомной цитаты")


@router.message(Command("random"))
async def cmd_random(message: Message):
	quote = await get_random_quote()
	if quote:
		await message.answer(f"{quote.text}\n - {quote.author}")
	else:
		await message.answer("В базе пока нет цитат.")

