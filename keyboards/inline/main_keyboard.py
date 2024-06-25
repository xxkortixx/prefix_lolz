from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def keyboard_main() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
            text="➕Добавить заметку",
            callback_data="add_note")
    )
    builder.add(types.InlineKeyboardButton(
            text="📖Мои заметки",
            callback_data="all_notes")
    )
    builder.add(types.InlineKeyboardButton(
            text="🔍Найти заметку",
            callback_data="search_note")
    )
    builder.add(types.InlineKeyboardButton(
            text="🗑️Удалить заметку",
            callback_data="delete_note")
    )
    builder.adjust(2)
    return builder.as_markup()


def keyboard_done() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
            text="➕Добавить заметку",
            callback_data="done")
    )
    builder.add(types.InlineKeyboardButton(
            text="Меню",
            callback_data="back")
    )
    builder.adjust(1)
    return builder.as_markup()


def keyboard_delete(id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
            text="✅Удалить",
            callback_data=f"delete:{id}")
    )
    builder.add(types.InlineKeyboardButton(
            text="Меню",
            callback_data="back")
    )
    builder.adjust(1)
    return builder.as_markup()


def keyboard_back_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
            text="Меню",
            callback_data="back")
    )
    builder.adjust(2)
    return builder.as_markup()
