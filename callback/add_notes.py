from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards.inline.main_keyboard import keyboard_done
from database.db import create_note

router = Router()


class Notes(StatesGroup):
    name_note = State()
    text = State()

"""FSM для добавления заметки в бд"""
@router.callback_query(F.data == "add_note")
async def add_note(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("📝Введите название заметки")
    await state.set_state(Notes.name_note)


@router.message(Notes.name_note)
async def state_name_note(message: types.Message, state: FSMContext):
    await state.update_data(name_note=message.text)
    await message.answer("📝Введите заметку")
    await state.set_state(Notes.text)


@router.message(Notes.text)
async def state_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    reply_markup = keyboard_done()
    await message.answer("Нажмите на кнопку что бы подтвердить действие", reply_markup=reply_markup)

"""Кнопка подтверждения добавления заметки"""
@router.callback_query(F.data == "done")
async def button_done(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await create_note(name_note=data['name_note'], text=data['text'])
    await state.clear()
    await callback.message.edit_text(text="Заметка успешно добавлена!")
