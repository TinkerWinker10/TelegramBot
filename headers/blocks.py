from aiogram import types
from aiogram.dispatcher import FSMContext
import markups as nav
from dispatcher import dp


@dp.message_handler(lambda message: message.text == '☀️Weather Broadcasts☀️')
async def weather_news(message: types.Message):
    await message.answer("Weather Broadcast was chosen ", reply_markup=nav.weatherMenu)


@dp.message_handler(lambda message: message.text == "💶Exchange Rates💶")
async def exchange_rates(message: types.Message):
    await message.answer("Exchange Rates was chosen", reply_markup=nav.exchangeMenu)


@dp.message_handler(lambda message: message.text == "🌐Recent News🌐")
async  def recent_news(message: types.Message):
    await  message.answer("Recent news was chosen, choose channel", reply_markup=nav.newsMenu)
