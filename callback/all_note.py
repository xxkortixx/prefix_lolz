from aiogram import Router, F, types

from database.db import all_note, info_note
from keyboards.inline.main_keyboard import keyboard_back_menu


router = Router()


@router.callback_query(F.data == "all_notes")
async def all_notes_list(callback: types.CallbackQuery):
    """ Обработчик кнопки Все заметки"""
    await callback.message.edit_text("Все заметки", reply_markup=await all_note())


@router.callback_query(F.data.startswith("note:"))
async def button_info_notes(callback: types.CallbackQuery):
    """ Обработчик нажатия определенной заметки и вывод ее содержания"""
    id = int(callback.data.split(":")[1])
    info = await info_note(id)
    await callback.message.edit_text(f"Название - {info[1]}\nСодержание - {info[2]}", reply_markup = keyboard_back_menu())
