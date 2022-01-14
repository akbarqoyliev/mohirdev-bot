import logging
import sqlite3
# import asyncpg
from loader import dp, db, bot
from data.config import ADMINS

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startMenu import menuStart


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # logging.info(message)
    # logging.info(f"{message.from_user.username=}")
    # logging.info(f"{message.from_user.full_name=}")
    # try:
    #     user = await db.add_user(telegram_id=message.from_user.id,
    #                              full_name=message.from_user.full_name,
    #                              username=message.from_user.username)
    # except asyncpg.exceptions.UniqueViolationError:
    #     user = await db.select_user(telegram_id=message.from_user.id)

    # # await message.answer("Xush kelibsiz!")

    # # ADMINGA xabar beramiz
    # count = await db.count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)

    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    # await message.answer("Xush kelibsiz!")
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    await message.answer(f"Assalom alaykum, {message.from_user.full_name}\n"
                          "Mohirdev.uz — " 
                          "Onlayn ta'lim platformasining Telegram botiga xush kelibsiz!",reply_markup=menuStart)
    await message.answer(f"O'zingizga kerakli bo'limni tanlang")
