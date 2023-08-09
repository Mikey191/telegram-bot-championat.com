"""
Функция команды start. При вызове этой команды выходит сообщение с кнопками /news
Функция команды news. При вызове этой команды выходит сообщение с инлайн клавиатурой где идет выбор Команды
"""
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_ikb import inkb_teams, inkb_teams_three, inkb_numbers
from keyboards.client_kb import kb_client
from aiogram.dispatcher.filters import Text
from pars.news import pars_last_club_news, pars_last_three_news, pars_news_href #тут происходит задвоение
# from pars import news
from data_base import sqlite_db

async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Твой выбор?", reply_markup=kb_client)

async def command_news(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбирите команду:", reply_markup=inkb_teams)

async def command_three_news(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбирите команду:", reply_markup=inkb_teams_three)

# @dp.callback_query_handler(Text(startswith="team_"))
async def team_last_news(callback: types.CallbackQuery):
    """
    Функция возвращает название последней новости с чампионата в виде сообщения в телеграме
    :param callback:
    :return:
    """
    print(f"Уловили хендлер: {callback.data}")
    print(f"Его вторая часть: {str(callback.data.split('_')[1])}")
    d = pars_last_club_news(str(callback.data.split("_")[1]))
    message_for_user = f"{d['date']}\n{d['time']}\n{d['news']}"
    await callback.message.answer(message_for_user)
    await callback.answer()

async def team_three_news(callback: types.CallbackQuery):
    """
    Функция возвращает последнии три пронумерованные новости о команде в виде сообщения в телеграме
    :param callback:
    :return:
    """
    print("team_three_news")
    d = pars_last_three_news(str(callback.data.split("_")[1]))
    print(type(d))

    message_for_user = f"{d['1']['number']}.\t{d['1']['news']}" + f"\n\n{d['2']['number']}.\t{d['2']['news']}" + f"\n\n{d['3']['number']}.\t{d['3']['news']}"
    await callback.message.answer(message_for_user, reply_markup=inkb_numbers)


async def any_of_three_news(callback: types.CallbackQuery):
    """
    Функция запускает функцию парсинга новости по номеру ссылки. И выводит результат в сообщение
    :param callback:
    :return:
    """
    d = pars_news_href(str(callback.data.split("_")[1]))
    message_for_user = f"{d['news']}\n\n{d['date']} {d['time']}"
    if d['photo'] == None:
        await callback.message.answer(message_for_user, reply_markup=kb_client)
    else:
        await callback.message.answer_photo(photo=d['photo'])
        await callback.message.answer(message_for_user, reply_markup=kb_client)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(command_news, commands=["last_news"])
    dp.register_message_handler(command_three_news, commands=["three_news"])
    dp.register_callback_query_handler(team_last_news, Text(startswith="team_"))
    dp.register_callback_query_handler(team_three_news, Text(startswith="three_"))
    dp.register_callback_query_handler(any_of_three_news, Text(startswith="number_"))
