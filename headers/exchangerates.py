from aiogram import types
from aiogram.dispatcher import FSMContext
import markups as nav
from dispatcher import dp
from states import ExchangeState
from exchange import get_rates


@dp.message_handler(lambda message: message.text == "💸Currency Rate💸")
async def weather_news(message: types.Message):
    await ExchangeState.ExchangeInfo.set()
    await message.answer("Currency Rates was chosen,\nEnter name of currency", reply_markup=nav.forecastMenu)


@dp.message_handler(state=ExchangeState.ExchangeInfo)
async def get_currency(message: types.Message, state:FSMContext):
    await ExchangeState.ExchangeInfo.set()
    async with state.proxy() as data:
        data["base"] = message.text
    await message.answer(get_rates(data["base"]), reply_markup=nav.exchangeMenu)
    await state.finish()


