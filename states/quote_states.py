from aiogram.fsm.state import StatesGroup, State

class QuotesStates(StatesGroup):
	adding_quote = State()
	deleting_quote = State()