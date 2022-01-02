from requests.api import get
from config import URL_EXCHANGE
import requests


def get_rates(base: str)->dict:
    data = requests.get(URL_EXCHANGE, locals()).json()
    if base not in data["rates"]:
        return f'Wrong currency name. Try again!'
    return f'Price per one {base}\nUSD: {data["rates"]["USD"]}\nEUR: {data["rates"]["EUR"]}\nGBP: {data["rates"]["GBP"]}'


def get_currency_by_ammount(base: str, second: str, ammount: str):
    keys = {'base':base, 'symbols':second, 'amount':ammount}
    data = requests.get(URL_EXCHANGE, params=keys).json()
    return f'Price of {ammount} {base} in {second}: {data["rates"][f"{second}"]}'



def get_data(base: str)->dict:
    data = requests.get(URL_EXCHANGE, locals()).json()
    return data
