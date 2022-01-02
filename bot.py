from aiogram import Dispatcher, Bot, types, executor
from aiogram.dispatcher import storage
from aiogram.dispatcher.storage import FSMContext
from bs4 import BeautifulSoup
import requests
from config import *
from exchange import *
import markups as nav
from weather import *
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot,storage = storage)



class States(StatesGroup):
    CurrentWeather = State()
    ForecastWeather = State()
    

class ExchangeState(StatesGroup):
    ExchangeInfo = State()
    ExchangeBase = State()
    ExchangeAdd = State()
    ExchangeAmm = State()

@dp.message_handler(lambda message: message.text == "Main menu", state = "*")
async def back_to_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Back to menu", reply_markup=nav.mainMenu)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply(
        "Hello, it's a bot, which can send you <b>latest news</b>, <b>weather broadcats</b> and <b>exchange rates</b>!",
        parse_mode=types.ParseMode.HTML)
    await message.answer("What you want to choose?", reply_markup=nav.mainMenu)


@dp.message_handler(commands=['help'])
async def help_handler():
    """
    help handler
    """
    pass


@dp.message_handler(lambda message: message.text == "Weather Broadcasts")
async def weather_news(message: types.Message):
    await message.answer("Weather Broadcast was chosen ",reply_markup=nav.weatherMenu)


@dp.message_handler(lambda message: message.text == "Current Weather")
async def weather_news(message: types.Message):
    await States.CurrentWeather.set()
    await message.answer("Current Weather was chosen,\n Enter your location:", reply_markup=nav.currentWeatherMenu)



@dp.message_handler(lambda message: message.text == "Weather Forecast")
async def weather_news(message: types.Message):
    await States.ForecastWeather.set()
    await message.answer("Weather Broadcast was chosen,\n Enter your location:", reply_markup=nav.forecastMenu)


@dp.message_handler(state=States.ForecastWeather)
async def get_location(message: types.Message, state:FSMContext):
    await States.ForecastWeather.set()
    async with state.proxy() as data:
        data['weather'] = message.text
    value = weather_forecast(data["weather"])
    if value != "Ooops. Wrong city name. Try again":
        await message.answer(weather_forecast(data["weather"]), reply_markup=nav.weatherMenu)
        await state.finish()
   

@dp.message_handler(state=States.CurrentWeather)
async def get_location(message: types.Message, state:FSMContext):
    await States.CurrentWeather.set()
    async with state.proxy() as data:
        data['weather'] = message.text
    value = current_weather(data["weather"])
    if value != "Ooops. Wrong city name. Try again":
        await message.answer(current_weather(data["weather"]), reply_markup=nav.weatherMenu)
        await state.finish()


@dp.message_handler(lambda message: message.text == "Exchange Rates")
async def exchange_rates(message: types.Message):
    await message.answer("Exchange Rates was chosen", reply_markup=nav.exhangeMenu)


#Exchange Ammount
    
@dp.message_handler(lambda message: message.text == "Exchange Ammount")
async def weather_news(message: types.Message):
    await ExchangeState.ExchangeBase.set()
    await message.answer("Exchange Ammount was chosen,\nEnter base currency", reply_markup=nav.forecastMenu)

@dp.message_handler(state=ExchangeState.ExchangeBase)
async def get_currency(message: types.Message, state:FSMContext):
    await ExchangeState.ExchangeBase.set()
    if message.text not in get_data("message.text")["rates"]:
        await message.answer("Wrong base")
    else:
        async with state.proxy() as data: 
            data["base"] = message.text
        await ExchangeState.next()
        await message.answer("Enter second currency")

@dp.message_handler(state=ExchangeState.ExchangeAdd)
async def get_currency(message: types.Message, state:FSMContext):
    if message.text not in get_data("message.text")["rates"]:
        await message.answer("Wrong base")
    else:
        async with state.proxy() as data: 
            data["second"] = message.text
        await ExchangeState.next()
        await message.answer("Enter ammount of base currency")


@dp.message_handler(state=ExchangeState.ExchangeAmm)
async def get_currency(message: types.Message, state:FSMContext):
    if message.text.isdigit(): 
        async with state.proxy() as data: 
            data["ammount"] = message.text
        await message.answer(get_currency_by_ammount(data["base"], data["second"], data["ammount"]), reply_markup=nav.exhangeMenu)
        await state.finish()
    else: 
        await message.answer("Ammount must be a decimal")


 
@dp.message_handler(lambda message: message.text == "Currency Rate")
async def weather_news(message: types.Message):
    await ExchangeState.ExchangeInfo.set()
    await message.answer("Currency Rates was chosen,\nEnter name of currency", reply_markup=nav.forecastMenu)

@dp.message_handler(state=ExchangeState.ExchangeInfo)
async def get_currency(message: types.Message, state:FSMContext):
    await ExchangeState.ExchangeInfo.set()
    async with state.proxy() as data: 
        data["base"] = message.text
    await message.answer(get_rates(data["base"]), reply_markup=nav.exhangeMenu)
    await state.finish()


@dp.message_handler(lambda message: message.text == "Recent News")
async def latest_news(message: types.Message):
    URL = 'https://www.unian.ua/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = soup.findAll('a', 'list-news__title')

    for i in range(0, len(texts[:-20])):
        txt = str(i + 1) + ') ' + texts[i].text
        await bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode='html')



if __name__ == "__main__":
    executor.start_polling(dp)