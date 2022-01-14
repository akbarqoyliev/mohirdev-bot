from loader import dp
from aiogram import types
from aiogram.types import Message, CallbackQuery, inline_keyboard, reply_keyboard

from keyboards.default.assistantKeyboards import cancel_button
from keyboards.inline.practicumKeyboard import practicumMapkup
from keyboards.inline.callback_data import practicum_callback
from keyboards.inline.practicumKeyboard import for_practicum
from data.practicum import practicumImages, practicumInfo


@dp.message_handler(text_contains="Praktikum")
async def practicum_menu(message: Message):
    await message.answer(text="📝 Praktikum", reply_markup=cancel_button)
    await message.answer(text="Praktikum kurslar bo'limi 👇", reply_markup=practicumMapkup)

@dp.callback_query_handler(practicum_callback.filter(item_name='back_to_practicum'))
async def back_practicum(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Praktikum kurslar bo'limi 👇",reply_markup=practicumMapkup)

@dp.callback_query_handler(practicum_callback.filter())
async def show_practicum(call: CallbackQuery):
    await call.message.delete()
    name = call.data[call.data.index(':')+1:]
    keyboard = await for_practicum(name)
    await call.message.answer_photo(photo=practicumImages[name], caption=practicumInfo[name], reply_markup=keyboard)

