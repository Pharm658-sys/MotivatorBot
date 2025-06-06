from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, select, update, delete
from MotivatorBot.db.session import Base

class Quote(Base):
	__tablename__ = "quotes"
	id: Mapped[int] = mapped_column(primary_key=True)
	text: Mapped[str] = mapped_column(String, unique=True)
	author: Mapped[str] = mapped_column(String)

