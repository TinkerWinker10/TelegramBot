from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext


class States(StatesGroup):
    CurrentWeather = State()
    ForecastWeather = State()


class ExchangeState(StatesGroup):
    ExchangeInfo = State()
    ExchangeBase = State()
    ExchangeAdd = State()
    ExchangeAmm = State()

