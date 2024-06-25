from aiogram import Router, F, types

from database.db import del_list_note, delete_note, info_note
from keyboards.inline.main_keyboard import keyboard_delete

router = Router()


@router.callback_query(F.data == "delete_note")
async def button_list_delete_note(callback: types.CallbackQuery):
    """ Обработчик кнопки Удалить заметку"""
    reply_markup = await del_list_note()
    await callback.message.answer("Выберите заметку для удаления", reply_markup=reply_markup)


@router.callback_query(F.data.startswith("del_note:"))
async def button_delete_info(callback: types.CallbackQuery):
    """обработчик нажатия на кнопку, которая показывает информацию об удаляемой заметке
      и под сообщение находится кнопка с подтверждением"""
    id = int(callback.data.split(":")[1])
    reply_markup = keyboard_delete(id)
    info = await info_note(id)
    await callback.message.edit_text(f"Название - {info[1]}\nСодержание - {info[2]}", reply_markup=reply_markup)


@router.callback_query(F.data.startswith("delete:"))
async def confirm_delete_note(callback: types.CallbackQuery):
    """Подтверждение и удаление заметки"""
    id = int(callback.data.split(":")[1])
    await delete_note(id)
    await callback.message.edit_text("Заметка была удалена")
