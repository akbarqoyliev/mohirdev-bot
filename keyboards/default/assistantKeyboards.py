from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import callback_data


cancel_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚫 Bekor qilish')
        ],
    ],
    resize_keyboard=True
)