from MotivatorBot.db.session import Session
from MotivatorBot.db.session import Session
from MotivatorBot.db.models import Quote
from sqlalchemy import select, func, delete


# Добавление цитаты в базу данных
async def add_quote(text: str, author: str):
	async with Session() as session:
		session.add(Quote(text=text, author=author))
		await session.commit()

# Получение случайной цитаты из базы данных.
async def get_random_quote():
	async with Session() as session:
		random_func = func.random
		results = await session.execute(select(Quote).order_by(random_func()).limit(1)
		                                )
		return results.scalar_one_or_none()

# Удаление цитаты из базы данных
async def delete_quote(quote_id) -> bool:
	async with Session() as session:
		result = await session.execute(select(Quote).where(Quote.id == quote_id))
		quote = result.scalar_one_or_none()
		if quote:
			await session.delete(quote)
			await session.commit()
			return True
		return False
