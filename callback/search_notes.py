from aiogram import Router, F, types
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.db import search_note


router = Router()


@router.callback_query(F.data == "search_note")
async def search_notes(callback: types.CallbackQuery):
    await callback.message.answer("Что бы найти заметки содержащие определенное слово или символ используйте комнаду /search")


@router.message(Command('search'))
async def search_note_command(message: types.Message, command: CommandObject):
    """Обработчик команды /search который получает аргумент из сообщения пользователя
        и передает его в функцию которая ищет заметки содержащие данное слово"""
    key_word = command.args
    found_notes = await search_note(key_word)
    if found_notes:
        builder = InlineKeyboardBuilder()
        for note in found_notes:
            builder.add(types.InlineKeyboardButton(text=f"{note['name_note']}", callback_data=f"note:{note['id']}"))
        await message.answer("Найденные заметки:", reply_markup=builder.as_markup())
    else:
        await message.answer("Заметки не найдены")
