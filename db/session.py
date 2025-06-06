from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, DeclarativeBase
from MotivatorBot.app.config import settings

Baser = declarative_base()

engine = create_async_engine(settings.DATABASE_URL)

Session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
	pass


async def create_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)