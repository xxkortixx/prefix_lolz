import asyncpg
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from config import USER,PASSWORD,DB_NAME,HOST



async def connect_db():
    """
    Подключение к бд
    """
    conn = await asyncpg.connect(
            user=USER,
            password=PASSWORD,
            database=DB_NAME,
            host=HOST
        )
    return conn


async def create_note(name_note: str, text: str):
    """
    Запись заметки в базе данных
 
    Args:
        name_note (str): название заметки
        text (str): содержание заметки
    """
    conn = await connect_db()
    await conn.execute(
            '''INSERT INTO notes (name_note, text)
            VALUES($1, $2)''', name_note, text
        )


async def delete_note(id: int | str):
    """
    Удаление заметки из базы данных
 
    Args:
        id (int | str): id заметки
    """
    conn = await connect_db()

    await conn.execute(
            '''DELETE FROM notes WHERE id = $1''', id
        )


async def search_note(key_word: str) -> tuple[str, int]:
    """
    Ищет заметку по ключевому слову
 
    Args:
        key_words (str): Ключевое слово
 
    Returns:
        tuple(str, int) : Название и id заметок которые найдены
    """
    conn = await connect_db()

    found_notes = await conn.fetch('''SELECT name_note,id FROM notes WHERE name_note ILIKE $1''', f'%{key_word}%')
    return found_notes


async def all_note() -> InlineKeyboardMarkup:
    """
    Ищет все заметки и выводит их ввиде клавиатуры
    """
    conn = await connect_db()
    builder = InlineKeyboardBuilder()
    for id, name_note in await conn.fetch('''SELECT id, name_note FROM notes'''):
        builder.add(
            types.InlineKeyboardButton(text=f"{name_note}", callback_data=f"note:{id}")
        )
        builder.add(types.InlineKeyboardButton(
            text="Меню",
            callback_data="back")
        )
    builder.adjust(1)
    return builder.as_markup()


async def info_note(id: int) -> tuple[int, str, str]:
    """
    Ищет информацию о заметке
 
    Args:
        id(int): Id заметки
 
    Returns:
        tuple(int, str, str) : id заметки, название заметки, текст заметки
    """
    conn = await connect_db()
    for note_id, name_note, text in await conn.fetch('''SELECT id, name_note, text FROM notes WHERE id = $1''', id):
        return note_id, name_note, text


async def del_list_note() -> InlineKeyboardMarkup:
    """
    Показывает список заметок в виде кавиатуры которые можно удалить
    """
    conn = await connect_db()
    builder = InlineKeyboardBuilder()
    for id, name_note in await conn.fetch('''SELECT id, name_note FROM notes'''):
        builder.add(
            types.InlineKeyboardButton(text=f"{name_note}", callback_data=f"del_note:{id}")
        )
        builder.add(types.InlineKeyboardButton(
            text="Меню",
            callback_data="back")
        )
    builder.adjust(1)
    return builder.as_markup()
