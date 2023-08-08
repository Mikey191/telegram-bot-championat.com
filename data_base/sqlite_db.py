import sqlite3 as sq
import json

#Функция создания (или подключения если такая база уже есть)
def sql_start() -> None:
    global base, cur
    base = sq.connect("football_news.db")
    cur = base.cursor()
    if base:
        print("data base connected...")
    base.execute(
        "CREATE TABLE IF NOT EXISTS news_club(club TEXT PRIMARY KEY, news TEXT, date TEXT, time TEXT)")  # создать таблицу, если такой не существует

#Функция для добавления в базу данных
def sql_add_command() -> None:
    f = open(r"C:\Users\whymk\Desktop\projects\project7\data\team_news.json", encoding="utf-8")
    data = json.load(f)
    cur.execute("INSERT INTO news_club VALUES (?, ?, ?, ?)", tuple(data.values()))
    base.commit()

#Функция чтения из базы данных всей информации
def sql_read():
    return cur.execute("SELECT * FROM news_club").fetchall()

#Функция удаления из базы данных по ключю
def sql_delete(key):
    cur.execute("DELETE FROM news_club WHERE name == ?", (key,))
    base.commit()

