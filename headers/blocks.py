from aiogram import types
import markups as nav
from dispatcher import dp


@dp.message_handler(lambda message: message.text == nav.btnWeather)
async def weather_news(message: types.Message):
    await message.answer("Weather Broadcast was chosen ", reply_markup=nav.weatherMenu)


@dp.message_handler(lambda message: message.text == nav.btnExchange)
async def exchange_rates(message: types.Message):
    await message.answer("Exchange Rates was chosen", reply_markup=nav.exchangeMenu)


@dp.message_handler(lambda message: message.text == nav.btnNews)
async  def recent_news(message: types.Message):
    await  message.answer("Recent news was chosen, choose channel", reply_markup=nav.newsMenu)
