from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_news = KeyboardButton("/last_news")
kb_three_news = KeyboardButton("/three_news")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(kb_news).insert(kb_three_news)