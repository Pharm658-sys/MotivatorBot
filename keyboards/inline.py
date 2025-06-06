from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

admin_panel_kb = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="Добавить цитату", callback_data="add_quote")
	],
	[
		InlineKeyboardButton(text="Удалить цитату", callback_data="delete_quote")
	]
])

