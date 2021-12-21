import requests
from bs4 import BeautifulSoup
from pprint import pprint as print
import json


def getBlogNames(pageNumber):
    blogKeys = []
    blogValues = []
    blogNames = {}
    page = f"https://mohirdev.uz/blog"
    if pageNumber:
        page = f"https://mohirdev.uz/blog/page/{pageNumber}"
    r = requests.get(page)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    blogs = soup.find_all(class_="content-item-title")
    links_list = soup.find_all('a')
    for link in links_list:
        if 'href' in link.attrs and link.attrs['href'] in str(blogs):
            key = str(link.attrs['href']).replace('https://mohirdev.uz', '')
            key = key.strip('/')
            if key not in blogValues:
                blogValues.append(key)
    blogValues.remove('')
    blogKeys = [blogs[i].text for i in range(len(blogs))]
    for i in range(len(blogValues)):
        blogNames[blogKeys[i]] = blogValues[i]
    return blogNames

def getBlogPhotos(page_number):
    blogPhotos = {}
    page = f"https://mohirdev.uz/blog"
    if page_number:
        page = f"https://mohirdev.uz/blog/page/{page_number}"
    r = requests.get(page)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    details = soup.find_all(class_='blog-details-img col-sm-5')
    links_list = soup.find_all('a')
    for text in details:
        text = str(text)
        photo_url = text[text.index('data-lazy-src="')+15:]
        photo_url = photo_url[:photo_url.index('"')]
        blog_name = text[text.index("mohirdev.uz/")+12:]
        blog_name = blog_name[:blog_name.index('"')-1]
        blogPhotos[blog_name] = str(photo_url)
    return blogPhotos

def getArticle(blogName):
    page = f"https://mohirdev.uz/{blogName}"
    r = requests.get(page)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    # maqola sarlavhasini ajratib olish
    title = str(soup.find_all(class_="content-item-title"))
    title = title.replace(' class="content-item-title"','')
    title = title.rstrip('</h2>]')
    title = title.strip('[<h2>')
    title = f"<b>{title}</b>\n"
    # maqola matnini olish
    text = str(soup.get_text())
    start = text.index("Baham ko'ring") + 14
    end = text.index("Izoh")
    text = text[start:end]
    text = text.strip()
    text = f"<i>{text}</i>\n\n"
    # maqolani chiqqan vaqti
    date = str(soup.find_all(class_="blog-date-wrapper"))
    a = date.index('>') + 1
    date = date[a:]
    a = date.index('<')
    date = date[:a]
    date = date.strip()
    # maqolani yig'ish
    article = title
    article += text
    article += date
    return title

def getArticlePiece(blogName):
    output = {}
    page = f"https://mohirdev.uz/{blogName}"
    r = requests.get(page)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    # maqola rasmini olish
    # img = str(soup.find_all(class_="featured-wrap"))
    # m = img.index('https:')
    # n = img.index('.jpg')
    # img = img[m:n+4]
    # maqola sarlavhasini ajratib olish
    title = str(soup.find_all(class_="content-item-title"))
    title = title.replace(' class="content-item-title"','')
    title = title.rstrip('</h2>]')
    title = title.strip('[<h2>')
    title = f"<b>{title}</b>\n"
    # maqolani qisqacha matnini olish
    text = str(soup.get_text())
    start = text.index("Baham ko'ring") + 10
    text = text.strip()
    text = text[start:start + 200]
    while text:
        text = text[:len(text)-2]
        if text[-1] == ' ':
            break
    text = f"{text.strip()}\n\n"
    # maqolani chiqqan vaqti
    date = str(soup.find_all(class_="blog-date-wrapper"))
    a = date.index('>') + 1
    date = date[a:]
    a = date.index('<')
    date = date[:a]
    date = f"<code>{date.strip()}</code>"
    # maqolani yig'ish
    article = title
    article += text
    article += f"🔗Batafsil: https://mohirdev.uz/{blogName}\n\n"
    article += date
    output['article'] = article
    # output['img'] = img
    return output

if __name__ == '__main__':
    # for i in range(1,9):
    # print(getBlogNames(i))
    # print(getArticle("data-science-yol-xaritasi"))
    # print(getArticlePiece("data-science-yol-xaritasi"))
    for i in range(1,12):
        print(getBlogPhotos(i))