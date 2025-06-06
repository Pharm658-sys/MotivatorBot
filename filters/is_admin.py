from aiogram.filters import BaseFilter
from aiogram import Bot
from aiogram.types import Message


ADMINS_IDS = [972921997]

class ISAdmin(BaseFilter):
	async def __call__(self, message: Message, bot: Bot) -> bool:
		return message.from_user.id in ADMINS_IDS