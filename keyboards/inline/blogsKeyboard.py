from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import blog_callback
from data.categoryData import blogNames
from filters.getEditData import getBlogNames, getArticle


numbers = {0:'0️⃣', 1:'1️⃣', 2:'2️⃣', 3:'3️⃣', 4:'4️⃣', 5:'5️⃣', 6:'6️⃣', 7:'7️⃣', 8:'8️⃣', 9:'9️⃣'}

next_button = InlineKeyboardButton(text="➡️", callback_data="next")
back_button = InlineKeyboardButton(text="⬅️", callback_data="back")
delete_button = InlineKeyboardButton(text="❌", callback_data="delete")

def getBlogKeyboard(pageNumber):
    if pageNumber < len(blogNames):
        i = 0
        Blogs = blogNames[pageNumber]
        BlogsMenu = InlineKeyboardMarkup(row_width=1)
        for key, value in Blogs.items():
            BlogsMenu.insert(InlineKeyboardButton(text=key, callback_data=blog_callback.new(item_name=i)))
            i += 1
        BlogsMenu.insert(back_button)
        BlogsMenu.row_width = 3
        BlogsMenu.insert(getNumberButton(pageNumber+1))
        BlogsMenu.insert(next_button)
        return BlogsMenu
    else:
        return None

def getNumberButton(number):
    text = ''
    for i in str(number):
        text += numbers[int(i)]
    number_button = InlineKeyboardButton(text=text, callback_data=f"number{number}")
    return number_button
