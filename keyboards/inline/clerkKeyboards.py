from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def readingArticle(name):
    deleteKeyboard=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="❌", callback_data='delete'),
            ],
        ]
    )
    return deleteKeyboard