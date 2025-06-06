from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from MotivatorBot.db.crud import add_quote, delete_quote
from MotivatorBot.filters.is_admin import ISAdmin
from MotivatorBot.keyboards.inline import admin_panel_kb
from MotivatorBot.states.quote_states import QuotesStates
from aiogram.fsm.context import FSMContext

router = Router()



@router.message(F.text == "/start", ISAdmin())
async def cmd_start(message: Message):
	await message.answer("Привет Админ! Добро пожаловать в Админ-панель", reply_markup=admin_panel_kb)


# Хэндлер для добавление новой цитаты.
@router.message(F.text.startswith("/add"), ISAdmin())
async def add_quote_handler(message: Message):
	print("add_quote_handler triggered")
	text = message.text.removeprefix("/add").strip()
	author = message.from_user.full_name
	try:
		await add_quote(text=text, author=author)
		await message.answer("Цитата добавлена.")
	except Exception as e:
		await message.answer(f"Ошибка: {e}")

# Хэндлер для удаления цитаты из БД по id.
@router.message(F.text.startswith("/delete"), ISAdmin())
async def cmd_delete_quote(message: Message):
	try:
		quote_id = int(message.text.removeprefix("/delete").strip())
		success = await delete_quote(quote_id)
		if success:
			await message.answer(f"Цитата с ID {quote_id} удалена")
		else:
			await message.answer(f"Цитата с ID {quote_id} не найдена.")
	except ValueError:
		await message.answer("Неверный формат. Используй: /delete <id>")
	except Exception as e:
		await message.answer(f"Ошибка при удалении: {e}")


# Обработка FSM /add команды.
@router.callback_query(F.data == "add_quote", ISAdmin())
async def on_add_quote(callback: CallbackQuery, state: FSMContext):
	await callback.answer()
	await callback.message.answer("Введите текст цитаты:")
	await state.set_state(QuotesStates.adding_quote)

# Обработка FSM /delete команды.
@router.callback_query(F.data == "delete_quote", ISAdmin())
async def on_delete_quote(callback: CallbackQuery, state: FSMContext):
	await callback.answer()
	await callback.message.answer("Введите ID цитаты для удаления:")
	await state.set_state(QuotesStates.deleting_quote)


@router.message(QuotesStates.adding_quote)
async def process_adding_quotes(message: Message, state: FSMContext):
	text = message.text.strip()
	try:
		await add_quote(text=text, author=message.from_user.full_name)
		await message.answer("Цитата добавлена ✅")
	except Exception as e:
		await message.answer(f"Ошибка при добавлении: {e}")
		await state.clear()


@router.message(QuotesStates.deleting_quote)
async def process_deleting_quote(message: Message, state: FSMContext):
	try:
		quote_id = int(message.text.strip())
		success = await delete_quote(quote_id)
		if success:
			await message.answer("Цитата удалена")
		else:
			await message.answer("Цитата с таким ID не найдена")
	except Exception as e:
		await message.answer(f"Ошибка при удалении: {e}")
		await state.clear()