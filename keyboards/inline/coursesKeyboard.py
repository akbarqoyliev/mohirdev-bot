from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data
from keyboards.inline.callback_data import teacher_callback, course_callback
from data.coursesData import instuctors, instuctorCourses, courseTypes, courses


instuctorsKeyboard = InlineKeyboardMarkup(row_width=2)
for key, value in instuctors.items():
    instuctorsKeyboard.insert(InlineKeyboardButton(text=value, callback_data=teacher_callback.new(item_name=key)))
instuctorsKeyboard.insert(InlineKeyboardButton(text='⬅️ Ortga', callback_data=teacher_callback.new(item_name='back_to_courses')))

async def getTeacherCoursesKeyboard(teacher_nickname):
    teacherCourses = InlineKeyboardMarkup(row_width=1)
    for course in instuctorCourses[teacher_nickname]:
        teacherCourses.insert(InlineKeyboardButton(text=course,callback_data=course_callback.new(item_name=courses[course])))
    teacherCourses.insert(InlineKeyboardButton(text='⬅️ Ortga', callback_data=course_callback.new(item_name='back_to_teachers')))
    return teacherCourses

async def courses_list(type):
    courses = InlineKeyboardMarkup(row_width=1)
    for key, value in courseTypes[type].items():
        courses.insert(InlineKeyboardButton(text=key, callback_data=f'course:{value}'))
    courses.insert(InlineKeyboardButton(text='⬅️ Ortga', callback_data=course_callback.new(item_name='back_to_courses')))
    return courses

    