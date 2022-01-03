from aiogram import types
from aiogram.dispatcher import FSMContext
import markups as nav
from dispatcher import dp
from news import *


@dp.message_handler(lambda message: message.text == "🥇Tribuna🥇")
async def weather_news(message: types.Message):
    await message.answer(get_sport_news())


@dp.message_handler(lambda message: message.text == "📍TSN📍")
async def weather_news(message: types.Message):
    await message.answer(get_tsn_news())


