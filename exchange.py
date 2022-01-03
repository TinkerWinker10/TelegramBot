import requests
from config import URL_EXCHANGE


def get_rates(base: str) -> str:
    data = requests.get(URL_EXCHANGE, locals()).json()
    if base not in data["rates"]:
        return f'Wrong currency name. Try again!'
    return f'Price per one {base}\nUSD: {data["rates"]["USD"]}\nEUR: {data["rates"]["EUR"]}\nGBP: {data["rates"]["GBP"]}'


def get_currency_by_ammount(base: str, second: str, amount: str):
    keys = {'base': base, 'symbols': second, 'amount': amount}
    data = requests.get(URL_EXCHANGE, params=keys).json()
    return f'Price of {amount} {base} in {second}: {data["rates"][f"{second}"]}'


def get_data(base: str) -> dict:
    data = requests.get(URL_EXCHANGE, locals()).json()
    return data
