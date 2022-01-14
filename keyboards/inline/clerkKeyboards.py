from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import practicum_callback


async def readingArticle(name):
    deleteKeyboard=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="❌", callback_data='delete'),
            ],
        ]
    )
    return deleteKeyboard

