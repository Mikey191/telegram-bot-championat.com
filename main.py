"""
В ТГБоте клиент нажимает на название команды и ему приходит последняя новость о ней.
Две команды:
/start - приветствие
/news - "О какой команде хотите новость?" + ikb_client
клиент нажимает на название команды =>
это название передаеться в функцию парсинга =>
функция парсинга возвращает словарь с новостью =>
записывает его в базу данных
и
возвращает этот же словарь ТГ-функции для отправки клиету =>
клиент РАД!

"""

from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from handlers import client

async def on_startup(_):
    print("Start Bot...")
    sqlite_db.sql_start()

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
