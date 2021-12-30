from os import stat
from aiogram import Dispatcher, Bot, dispatcher, types, executor
from pprint import pprint
from aiogram.dispatcher import storage
from aiogram.dispatcher.storage import FSMContext
from bs4 import BeautifulSoup
import requests
from config import *
import markups as nav
from weather import *
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot,storage = storage)



class States(StatesGroup):
    weather = State()


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
    await States.weather.set()
    await message.answer("Current Weather was chosen,\n Enter your location? ", reply_markup=nav.currentWeatherMenu)



@dp.message_handler(lambda message: message.text == "Weather Forecast")
async def weather_news(message: types.Message):
    await message.answer("Weather Broadcast was chosen,\n Enter your location?", reply_markup=nav.forecastMenu)
   

@dp.message_handler(state=States.weather)
async def get_location(message: types.Message, state:FSMContext):
    await States.weather.set()
    async with state.proxy() as data:
        data['weather'] = message.text
    value = current_weather(data["weather"])
    if value != "Ooops. Wrong city name. Try again":
        await message.answer(current_weather(data["weather"]), reply_markup=nav.weatherMenu)
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


@dp.message_handler(lambda message: message.text == "Exchange Rates")
async def exchange_rates(message: types.Message):
    await message.answer("Exchange Rates was chosen", reply_markup=nav.exhangeMenu)



if __name__ == "__main__":
    executor.start_polling(dp)