import requests
from bs4 import BeautifulSoup
from pprint import pprint as print

def get_courses():
    courses = {}
    page = f"https://mohirdev.uz/courses/?tutor_course_filter=course_title_az"
    r = requests.get(page)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    r = soup.find_all('h3')
    for i in range(3,39):
        text = str(r[i])
        key = text[text.index('/">')+5:text.index('</a>')].strip()
        value = text[text.index('courses/')+8:text.index('/">')]
        courses[key] = value
    return courses

if __name__ == '__main__':
    print(get_courses())