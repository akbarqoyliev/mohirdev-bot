import requests
from bs4 import BeautifulSoup
from pprint import pprint as print
import json

def course_title(courseName):
    page = f"https://mohirdev.uz/courses/{courseName}"
    r = requests.get(page)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    courseTitles = soup.find_all(class_="lesson_title")
    titles = []
    for title in courseTitles:
        title = str(title)
        title = title[title.index('</i>')+5:]
        title = title[:title.index('</h4>')]
        titles.append(title)
    return titles

def course_lessons(courseName):
    page = f"https://mohirdev.uz/courses/{courseName}"
    r = requests.get(page)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    courseLessons = soup.find_all(class_="tutor-course-lesson-content")
    i = 1
    lessons = {}
    for lesson in courseLessons:
        lesson = str(lesson)
        if 'tutor-lesson-duration' in lesson:
            lesson = lesson[lesson.index('inner">')+7:]
            lesson = lesson[:lesson.index('<')]
            lessons[i] = lesson
            i += 1
    return lessons

def lesson_link(courseName):
    page = f"https://mohirdev.uz/courses/{courseName}/lesson/3-valid-anagram"
    r = requests.get(page)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('iframe'):
        print(link.get('src'))
    # link = soup.find_all('a', class_="tutor-col-8 tutor-col-md-100")
    # print(link)
    

if __name__ == '__main__':
    # print(course_title('django'))
    # print(course_lessons('django'))
    print(lesson_link('algoritmlar-leetcode-da-masala-yechish'))