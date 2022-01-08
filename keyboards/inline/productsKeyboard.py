from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


categoryCourses = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Dasturlash tillari", callback_data="programming_languages")
    ],
    [
        InlineKeyboardButton(text="👨‍🏫 O'qituvchilar", callback_data="teachers")
    ],
    [
        InlineKeyboardButton(text="🎁 Bepul kurslar", callback_data="free_courses"),
        InlineKeyboardButton(text="💸 Pullik kurslar", callback_data="paid_courses")
    ],
    [
        InlineKeyboardButton(text="🗂 Barcha kurslar ro'yxati", callback_data="courses"),
    ]
])