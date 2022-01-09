import logging
from os import replace
from typing import Text

from requests.api import delete
from loader import dp
from aiogram.types import Message, CallbackQuery, inline_keyboard, reply_keyboard
from aiogram.dispatcher import FSMContext

from keyboards.inline.productsKeyboard import categoryCourses
from keyboards.default.assistantKeyboards import cancel_button
from keyboards.default.startMenu import menuStart
from data.coursesData import instuctorsImage, instuctors
# from filters.getEditData import getBlogsName



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


@dp.message_handler(text='salom')
async def getPhoto(message: Message):
    for key in instuctorsImage.keys():
        await message.answer_video(video="https://player.vdocipher.com/playerAssets/1.x/vdo/embed/index.html#otp=20160313versASE323Rwda8jxTk9ksI1KtZybqWgjyJmU2G0qFBwNrf9OFtSwCJV&playbackInfo=eyJ2aWRlb0lkIjoiZjUzZmYzNTI3Njg5NGU5YmI4Njg1N2QyYWY5OTk1ZmQifQ==")
