from aiogram import types
from aiogram.dispatcher import FSMContext
import markups as nav
from dispatcher import dp
from states import ExchangeState
from exchange import get_data, get_currency_by_ammount


@dp.message_handler(lambda message: message.text == nav.btnExchangeAmount)
async def weather_news(message: types.Message):
    await ExchangeState.ExchangeBase.set()
    await message.answer("Exchange Amount was chosen,\nEnter base currency", reply_markup=nav.forecastMenu)


@dp.message_handler(state=ExchangeState.ExchangeBase)
async def get_currency(message: types.Message, state: FSMContext):
    await ExchangeState.ExchangeBase.set()
    if message.text not in get_data("message.text")["rates"]:
        await message.answer("Wrong base")
    else:
        async with state.proxy() as data:
            data["base"] = message.text
        await ExchangeState.next()
        await message.answer("Enter second currency")


@dp.message_handler(state=ExchangeState.ExchangeAdd)
async def get_currency(message: types.Message, state: FSMContext):
    if message.text not in get_data("message.text")["rates"]:
        await message.answer("Wrong base")
    else:
        async with state.proxy() as data:
            data["second"] = message.text
        await ExchangeState.next()
        await message.answer("Enter amount of base currency")


@dp.message_handler(state=ExchangeState.ExchangeAmm)
async def get_currency(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data["amount"] = message.text
        await message.answer(get_currency_by_ammount(data["base"], data["second"], data["amount"]),
                             reply_markup=nav.exchangeMenu)
        await state.finish()
    else:
        await message.answer("Amount must be a decimal")
