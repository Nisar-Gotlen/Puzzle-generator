import numpy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

NG_BUTT_ID = 'mapsubmit'                        # "New Game" button id


def get_content(html):

    numbers = []                                # Parsed numbers from the playing field
    soup = BeautifulSoup(html, 'html.parser')
    pole = soup.find('ul', class_='tab')
    items = pole.find_all('li')

    for item in items:
        try:
            numbers.append(int(item.get_text()))
        except ValueError:
            if item.get_text() == '':
                numbers.append(0)

    return numbers


def change_diff(driver, RB_ID):

    driver.find_element_by_id(RB_ID).click()
    driver.find_element_by_id(NG_BUTT_ID).click()
    time.sleep(1)
    return driver


def field_parse(RB_ID, driver):

    driver = change_diff(driver, RB_ID)
    html = driver.page_source
    numbers = get_content(html)
    puzzle = numpy.array(numbers)
    puzzle = numpy.reshape(puzzle, (9, 9))
    return puzzle
