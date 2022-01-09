from loader import dp
from aiogram import types
from aiogram.types import Message, CallbackQuery, inline_keyboard, reply_keyboard

from keyboards.default.assistantKeyboards import cancel_button
from keyboards.inline.practicumKeyboard import practicumMapkup


@dp.message_handler(text_contains="Praktikum")
async def select_course(message: Message):
    await message.answer(f"Praktikum kurslar bo'limi 👇", reply_markup=practicumMapkup)
    await message.answer(text="💻 Kurslar", reply_markup=cancel_button)

