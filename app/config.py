from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
	TOKEN = os.getenv("BOT_TOKEN")
	DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()