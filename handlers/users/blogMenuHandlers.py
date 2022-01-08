import logging
from re import A
from loader import dp

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import factory, state
from aiogram.types import Message, CallbackQuery, inline_keyboard, message

from keyboards.inline.blogsKeyboard import getBlogKeyboard
from keyboards.inline.callback_data import blog_callback
from keyboards.inline.clerkKeyboards import readingArticle
from keyboards.default.startMenu import menuStart
from states.blogPages import BlogState
from data.categoryData import blogNames, blogPhotos
from filters.getEditData import getArticle, getArticlePiece


@dp.callback_query_handler(text='back', state=BlogState.blogstate)
async def back_blog(call: CallbackQuery, state: FSMContext):  
    data = await state.get_data()
    page_num = data.get('page_number')
    if page_num != 0:
        page_num -= 1
        blog_menu = await getBlogKeyboard(page_num)
        await call.message.edit_reply_markup(reply_markup=blog_menu)
        await state.update_data(page_number=page_num)
    else:
        await call.answer("Siz allaqachon birinchi sahifadasiz", cache_time=60, show_alert=False)

@dp.callback_query_handler(text='next', state=BlogState.blogstate)
async def next_blog(call: CallbackQuery, state: FSMContext):  
    data = await state.get_data()
    page_num = data.get('page_number')
    if await getBlogKeyboard(page_num+1):
        page_num += 1
        blog_menu = await getBlogKeyboard(page_num)
        await call.message.edit_reply_markup(reply_markup=blog_menu)
        await state.update_data(page_number=page_num)
    else:
        await call.answer("Hech narsa topilmadi 😔", cache_time=60, show_alert=False)


@dp.callback_query_handler(blog_callback.filter(), state=BlogState.blogstate)
async def get_article(call: CallbackQuery, state: FSMContext):
    await call.answer("Maqola tayyorlanmoqda", cache_time=60, show_alert=False)
    data = await state.get_data()
    page_num = data.get('page_number')
    k = 0
    for value in blogNames[int(page_num)].values():
        if k == int(call.data[-1]):
            response = await getArticlePiece(value)
            keyboard = await readingArticle(value)
            photo = blogPhotos[value]
            break
        k += 1
    await call.message.delete()
    await call.message.answer_photo(photo=photo, caption=response['article'], reply_markup=keyboard)
    await call.message.answer(text='Maqola tanlang 👇',reply_markup=await getBlogKeyboard(page_num))

@dp.callback_query_handler(text='delete', state=BlogState.blogstate)
async def delete_article(call: CallbackQuery, state: FSMContext):  
    # await call.message.delete_reply_markup()
    await call.message.delete()

@dp.message_handler(text_contains='Bekor qilish', state=BlogState.blogstate)
async def cancel(message: Message, state: FSMContext):
    await message.answer(text="Kerakli bo'limni tanlang 👇",reply_markup=menuStart)
    await state.update_data(variable = False)
    await state.finish()

@dp.callback_query_handler(text='delete')
async def delete_article(call: CallbackQuery, state: FSMContext):  
    # await call.message.delete_reply_markup()
    await call.message.delete()






















# @dp.callback_query_handler(state=BlogPages.blogPage1)
# async def blog_page1(call: CallbackQuery):  
#     callData = call.data
#     if callData == 'cancel':
#         await call.answer("Siz allaqachon birinchi sahifadasiz",show_alert=False)
#     elif callData == 'next':
#         BlogsMenu = getBlogKeyboard(1)
#         await call.message.edit_reply_markup(reply_markup=BlogsMenu)
#         await BlogPages.blogPage2.set()
#     else:
#         await state.Optional()

# @dp.callback_query_handler(text=['cancel','next'], state=BlogPages.blogPage2)
# async def blog_page2(call: CallbackQuery):  
#     callData = call.data
#     if callData == 'cancel':
#         BlogsMenu = getBlogKeyboard(0)
#         await call.message.edit_reply_markup(reply_markup=BlogsMenu)
#         await BlogPages.blogPage1.set()
#     if callData == 'next':
#         BlogsMenu = getBlogKeyboard(2)
#         await call.message.edit_reply_markup(reply_markup=BlogsMenu)
#         await BlogPages.blogPage3.set()

# @dp.callback_query_handler(text=['cancel','next'], state=BlogPages.blogPage3)
# async def blog_page3(call: CallbackQuery):  
#     callData = call.data
#     if callData == 'cancel':
#         BlogsMenu = getBlogKeyboard(1)
#         await call.message.edit_reply_markup(reply_markup=BlogsMenu)
#         await BlogPages.blogPage2.set()
#     if callData == 'next':
#         BlogsMenu = getBlogKeyboard(3)
#         await call.message.edit_reply_markup(reply_markup=BlogsMenu)
#         await BlogPages.blogPage4.set()

# @dp.callback_query_handler(text=['cancel','next'], state=BlogPages.blogPage4)
# async def blog_page4(call: CallbackQuery):  
#     callData = call.data
#     if callData == 'cancel':
#         BlogsMenu = getBlogKeyboard(2)
#         await call.message.edit_reply_markup(reply_markup=BlogsMenu)
#         await BlogPages.blogPage3.set()
#     if callData == 'next':
#         BlogsMenu = getBlogKeyboard(4)
#         await call.message.edit_reply_markup(reply_markup=BlogsMenu)
#         await BlogPages.blogPage5.set()

# @dp.callback_query_handler(text=['cancel','next'], state=BlogPages.blogPage5)
# async def blog_page5(call: CallbackQuery):  
#     callData = call.data
#     if callData == 'cancel':
#         BlogsMenu = getBlogKeyboard(3)
#         await call.message.edit_reply_markup(reply_markup=BlogsMenu)
#         await BlogPages.blogPage4.set()
#     if callData == 'next':
#         await call.answer("Hech narsa topilmadi",show_alert=False)