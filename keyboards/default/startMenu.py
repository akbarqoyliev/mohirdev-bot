from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='💻 Kurslar'),
            KeyboardButton(text='📝 Praktikum'),
        ],
        [
            KeyboardButton(text='📋 Blog')
        ],
        [
            KeyboardButton(text='📜 Biz haqimizda')
        ],
        [
            KeyboardButton(text="🤝 Qo'llab quvvatlash")
        ],
    ],
    resize_keyboard=True
)