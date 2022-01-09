from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data
from keyboards.inline.callback_data import practicum_callback
from data.practicum import praticumDict

practicumMapkup = InlineKeyboardMarkup(row_width=1)
for key, value in praticumDict.items():
    practicumMapkup.insert(InlineKeyboardButton(text=key, callback_data=f"practicum:{value}"))
# practicumMapkup.insert(InlineKeyboardButton(text='⬅️ Ortga', callback_data='practicum:back'))