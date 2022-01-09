from loader import dp
from aiogram import types
from aiogram.types import Message, CallbackQuery, inline_keyboard, reply_keyboard

from keyboards.default.assistantKeyboards import cancel_button
from keyboards.inline.practicumKeyboard import practicumMapkup


@dp.message_handler(text_contains="Praktikum")
async def practicum_menu(message: Message):
    await message.answer(text="📝 Praktikum", reply_markup=cancel_button)
    await message.answer(text="Praktikum kurslar bo'limi 👇", reply_markup=practicumMapkup)

