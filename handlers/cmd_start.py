import asyncpg
from aiogram.filters import Command
from aiogram import types, Router
from config import host, user, password, db_name
from keyboards.inline.main_keyboard import keyboard_main

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start
    """
    conn = await asyncpg.connect(
            user=user,
            password=password,
            database=db_name,
            host=host
        )

    await conn.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id SERIAL PRIMARY KEY,
        text TEXT,
        name_note TEXT
    )''')

    reply_markup = keyboard_main()
    await message.answer(text="Привет rszx!", reply_markup=reply_markup)