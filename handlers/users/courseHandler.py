from aiogram import types
# from aiogram.dispatcher.filters import state
from requests.api import get
from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from data.coursesData import instuctorsImage, instuctors
# from states.categories import TeacherState
from keyboards.inline.coursesKeyboard import instuctorsKeyboard, getTeacherCoursesKeyboard, courses_list
from keyboards.inline.callback_data import teacher_callback, course_callback
from keyboards.inline.productsKeyboard import categoryCourses
from keyboards.default.assistantKeyboards import cancel_button

@dp.callback_query_handler(text='teachers')
async def get_teachers_keyboard(call: CallbackQuery):  
    await call.message.edit_reply_markup(reply_markup=instuctorsKeyboard)

@dp.callback_query_handler(teacher_callback.filter(item_name='back_to_courses'))
async def back_courses(call: CallbackQuery, state: FSMContext):  
    await call.message.edit_reply_markup(reply_markup=categoryCourses)

@dp.callback_query_handler(teacher_callback.filter())
async def get_teacher_courses(call: CallbackQuery):
    teacher_nickname = str(call.data)[8:]
    if teacher_nickname in instuctors.keys():
        teacherCourses = await getTeacherCoursesKeyboard(teacher_nickname)
        await call.message.edit_reply_markup(reply_markup=teacherCourses)

@dp.callback_query_handler(course_callback.filter(item_name='back_to_teachers'))
async def back_teachers(call: CallbackQuery):  
    await call.message.edit_reply_markup(reply_markup=instuctorsKeyboard)

@dp.callback_query_handler(text='programming_languages')
async def programming_languages_handler(call: CallbackQuery):
    courses = await courses_list('programming_languages')
    await call.message.edit_reply_markup(reply_markup=courses)

@dp.callback_query_handler(text='free_courses')
async def free_courses_handler(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=await courses_list('free_courses'))

@dp.callback_query_handler(text='paid_courses')
async def paid_courses_handler(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=await courses_list('paid_courses'))

@dp.callback_query_handler(text='courses')
async def courses_handler(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=await courses_list('courses'))

# kurlar bo'limiga qaytish
@dp.callback_query_handler(course_callback.filter(item_name='back_to_courses'))
async def back_courses(call: CallbackQuery):  
    await call.message.edit_reply_markup(reply_markup=categoryCourses)

# @dp.callback_query_handler(course_callback.filter())
# async def get_courses(call: CallbackQuery):
