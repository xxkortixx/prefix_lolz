from aiogram import Router, F, types

from keyboards.inline.main_keyboard import keyboard_main


router = Router()


@router.callback_query(F.data == "back")
async def back_main_menu(callback: types.CallbackQuery):
    """Кнопка которая возвращает пользователя в меню"""
    reply_markup = keyboard_main()
    await callback.message.edit_text(text="Меню:", reply_markup=reply_markup)
