from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def readingArticle(name):
    deleteKeyboard=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="❌", callback_data='delete'),
            ],
        ]
    )
    return deleteKeyboard