from aiogram import types
from aiogram.dispatcher import FSMContext
import markups as nav
from dispatcher import dp
from states import States
from weather import current_weather


@dp.message_handler(lambda message: message.text == '⛈Current Weather⛈')
async def weather_news(message: types.Message):
    await States.CurrentWeather.set()
    await message.answer("Current Weather was chosen,\n Enter your location:", reply_markup=nav.currentWeatherMenu)


@dp.message_handler(state=States.CurrentWeather)
async def get_location(message: types.Message, state: FSMContext):
    await States.CurrentWeather.set()
    async with state.proxy() as data:
        data['weather'] = message.text
    value = current_weather(data["weather"])
    if value != "Oops. Wrong city name. Try again":
        await message.answer(current_weather(data["weather"]), reply_markup=nav.weatherMenu)
        await state.finish()
