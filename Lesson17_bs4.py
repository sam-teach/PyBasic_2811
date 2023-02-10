"""
парсер для сайта (auto.ria.com)
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/car/used/?page='


def get_html(url: str = URL):
    """
    Getting html from url
    :param url:
    :return: html or status code(if not 200)
    """
    data = requests.get(url)
    if data.status_code == 200:
        return data.text
    return data.status_code


def get_cars_from_page(url):
    html_text = get_html(url)
    soup = BeautifulSoup(html_text, 'html.parser')
    all_cars = soup.find_all('div', class_='content-bar')
    for one_auto in all_cars:
        if one_auto.find('a').get('class') == ['banner-link']:
            continue
        print(one_auto.find('span', class_='blue bold').text, end=':')
        # print(one_auto.find('span', class_='bold size22 green').text)
        print(one_auto.find('div', class_='price-ticket').get('data-main-price'), end=':')
        # print(one_auto.find('li', class_='item-char js-race').text)
        # print(one_auto.find('li', class_='item-char view-location js-location').text)
        technical_data = one_auto.find_all('li', class_='item-char')
        for item in technical_data:
            if item.find('i', class_='icon-mileage') != None:
                print(item.text, end=':')
            if item.find('i', class_='icon-location') != None:
                print(item.text, end=':')
            if item.find('i', class_='icon-fuel') != None:
                print(item.text, end=':')
            if item.find('i', title='Тип коробки передач') != None:
                print(item.text, end=':')
        print(one_auto.find('a').get('href'))


for i in range(1, 4):
    print(f'read page {i}...')
    get_cars_from_page(URL + str(i))
    print('DONE!!!')
