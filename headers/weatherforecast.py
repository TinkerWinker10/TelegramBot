from aiogram import types
from aiogram.dispatcher import FSMContext
import markups as nav
from dispatcher import dp
from states import States
from weather import weather_forecast


@dp.message_handler(lambda message: message.text == '🌪Weather Forecast🌪')
async def weather_news(message: types.Message):
    await States.ForecastWeather.set()
    await message.answer("Weather Broadcast was chosen,\n Enter your location:", reply_markup=nav.forecastMenu)


@dp.message_handler(state=States.ForecastWeather)
async def get_location(message: types.Message, state:FSMContext):
    await States.ForecastWeather.set()
    async with state.proxy() as data:
        data['weather'] = message.text
    value = weather_forecast(data["weather"])
    if value != "Oops. Wrong city name. Try again":
        await message.answer(weather_forecast(data["weather"]), reply_markup=nav.weatherMenu)
        await state.finish()

