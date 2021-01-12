import numpy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://sudoku.org.ua/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Accept': '*/*'
}
numbers = []


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(html):

    soup = BeautifulSoup(html, 'html.parser')
    pole = soup.find('ul', class_='tab')
    items = pole.find_all('li')

    for item in items:
        try:
            numbers.append(int(item.get_text()))
        except ValueError:
            if item.get_text() == '':
                numbers.append(0)

    puzzle = numpy.array(numbers)
    puzzle = numpy.reshape(puzzle, (9, 9))
    return puzzle


def parse():
    driver = webdriver.Edge('D:\Apps\msedgedriver.exe')
    driver.get(URL)
    html = driver.page_source
    get_content(html)
