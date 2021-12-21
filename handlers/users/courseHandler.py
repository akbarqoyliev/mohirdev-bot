from aiogram import types
# from aiogram.dispatcher.filters import state
from requests.api import get
from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from data.coursesData import instuctorsImage, instuctors
# from states.categories import TeacherState
from keyboards.inline.coursesKeyboard import instuctorsKeyboard, getTeacherCoursesKeyboard
from keyboards.inline.callback_data import teacher_callback, course_callback
from keyboards.inline.productsKeyboard import categoryCourses
from keyboards.default.assistantKeyboards import cancel_button

@dp.callback_query_handler(text='teachers')
async def get_teachers_keyboard(call: CallbackQuery):  
    await call.message.edit_reply_markup(reply_markup=instuctorsKeyboard)

@dp.callback_query_handler(teacher_callback.filter(item_name='back'))
async def back_courses(call: CallbackQuery, state: FSMContext):  
    await call.message.edit_reply_markup(reply_markup=categoryCourses)

@dp.callback_query_handler(teacher_callback.filter())
async def get_teacher_courses(call: CallbackQuery):
    teacher_nickname = str(call.data)[8:]
    if teacher_nickname in instuctors.keys():
        teacherCourses = getTeacherCoursesKeyboard(teacher_nickname)
        await call.message.edit_reply_markup(reply_markup=teacherCourses)

@dp.callback_query_handler(course_callback.filter(item_name='back'))
async def back_teachers(call: CallbackQuery):  
    await call.message.edit_reply_markup(reply_markup=instuctorsKeyboard)

# @dp.callback_query_handler(course_callback.filter())
# async def get_courses(call: CallbackQuery):
