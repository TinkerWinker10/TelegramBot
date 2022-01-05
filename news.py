import requests
from bs4 import BeautifulSoup


def get_tsn_news():
    url = 'https://tsn.ua/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='c-card__link')

    news = {}
    for i in quotes[:10]:
        news[i.text.strip()] = i["href"]

    return "\n".join(list(map(str, [str(k) + ': ' + str(v) for k, v in news.items()])))


def get_tribuna_news():
    url = 'https://ua.tribuna.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='h2')
    news = {}
    for i in quotes[:10]:
        news[i.text.strip()] = i["href"]

    return "\n".join(list(map(str, [str(k) + ': ' + str(v) for k, v in news.items()])))


def get_unian_news():
    url = 'https://www.unian.ua/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='list-news__title')
    news = {}
    for i in quotes[:10]:
        news[i.text.strip()] = i["href"]

    return "\n".join(list(map(str, [str(k) + ': ' + str(v) for k, v in news.items()])))


def get_bbc_news():
    url = 'https://www.bbc.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='block-link__overlay-link')
    news = {}
    for i in quotes[:10]:
        news[i.text.strip()] = url + (i["href"])[1:]

    return "\n".join(list(map(str, [str(k) + ': ' + str(v) for k, v in news.items()])))


def get_sport_news():
    url = 'https://sport.ua/uk'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='main-news__title')
    news = {}
    for i in quotes[:10]:
        news[i.text.strip()] = i["href"]

    return "\n".join(list(map(str, [str(k) + ': ' + str(v) for k, v in news.items()])))
