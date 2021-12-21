import logging
from loader import dp

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startMenu import menuStart


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")
    await message.answer(f"Assalom alaykum, {message.from_user.full_name}\n"
                          "Mohirdev.uz — " 
                          "Onlayn ta'lim platformasining Telegram botiga xush kelibsiz!",reply_markup=menuStart)
    await message.answer(f"O'zingizga kerakli bo'limni tanlang")
