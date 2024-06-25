import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from config import TOKEN
from handlers import cmd_start
from callback import add_notes, search_notes, all_note, delete_note, back_menu

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher()

dp.include_routers(cmd_start.router, add_notes.router, search_notes.router,
                    all_note.router, delete_note.router, back_menu.router)


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
