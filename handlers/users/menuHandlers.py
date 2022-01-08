import logging
from os import replace
from typing import Text

from requests.api import delete
from loader import dp
from aiogram.types import Message, CallbackQuery, inline_keyboard, reply_keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import factory, state

from keyboards.inline.productsKeyboard import categoryCourses
from keyboards.inline.blogsKeyboard import getBlogKeyboard
from keyboards.inline.callback_data import blog_callback
from keyboards.default.assistantKeyboards import cancel_button
from keyboards.default.startMenu import menuStart
from states.blogPages import BlogState
from data.coursesData import instuctorsImage, instuctors
# from filters.getEditData import getBlogsName


@dp.message_handler(text_contains="Blog", state=None)
async def select_blog(message: Message, state: FSMContext):
    BlogsMenu = await getBlogKeyboard(0)
    await message.answer(f"{message.text}", reply_markup=cancel_button)
    await message.answer(text='Maqola tanlang 👇',reply_markup=BlogsMenu)
    await BlogState.blogstate.set()
    await state.update_data(page_number=0)

@dp.message_handler(text_contains="Kurslar")
async def select_course(message: Message):
    await message.answer(text="💻 Kurslar",reply_markup=cancel_button)
    await message.answer(f"Kerakli kurs bo'limini tanlang", reply_markup=categoryCourses)

@dp.message_handler(text="📜 Biz haqimizda")
async def get_about(message: Message):
    await message.answer(text=f"<a href='https://telegra.ph/Biz-Haqimizda-12-21'>Biz Haqimizda</a>")

@dp.message_handler(text="🤝 Qo'llab quvvatlash")
async def get_about(message: Message):
    text = "Qo’llab-quvvatlash\n"
    text += "👥 <a href='https://t.me/mohirdev'>Mohirlar jamiyati – Telegram</a>\n"
    text += " ⓕ  <a href='https://www.facebook.com/groups/mohirdev'>Mohirdev jamiyati – Facebook</a>\n"
    text += "📣 <a href='https://t.me/mohirdev'>Telegram kanal</a>\n"
    text += "🤖 <a href='https://t.me/mohirdev_bot'>Savol va takliflar uchun bot</a>\n"
    text += "📍 <a href='https://www.google.com/maps?cid=6451963227536757315'>Bizning manzil</a>"
    await message.answer(text=text,disable_web_page_preview=True)

@dp.message_handler(text_contains='Bekor qilish')
async def cancel(message: Message):
    await message.answer(text="Kerakli bo'limni tanlang 👇",reply_markup=menuStart)


# @dp.message_handler(text='salom')
# async def getPhoto(message: Message):
#     for key in instuctorsImage.keys():
#         await message.answer_photo(photo=instuctorsImage[key],caption=instuctors[key])
