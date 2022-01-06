from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data
from keyboards.inline.callback_data import teacher_callback, course_callback
from data.coursesData import instuctors, instuctor_courses, coursesList


instuctorsKeyboard = InlineKeyboardMarkup(row_width=1)
for key, value in instuctors.items():
    instuctorsKeyboard.insert(InlineKeyboardButton(text=value, callback_data=teacher_callback.new(item_name=key)))
instuctorsKeyboard.insert(InlineKeyboardButton(text='⬅️ Ortga', callback_data=teacher_callback.new(item_name='back')))

async def getTeacherCoursesKeyboard(teacher_nickname):
    teacherCourses = InlineKeyboardMarkup(row_width=1)
    for course in instuctor_courses[teacher_nickname]:
        teacherCourses.insert(InlineKeyboardButton(text=course,callback_data=course_callback.new(item_name=coursesList[course])))
    teacherCourses.insert(InlineKeyboardButton(text='⬅️ Ortga', callback_data=course_callback.new(item_name='back')))
    return teacherCourses