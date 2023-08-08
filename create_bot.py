from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from data.config_telegram import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)