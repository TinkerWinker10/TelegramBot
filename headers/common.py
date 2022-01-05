from aiogram import types
from aiogram.dispatcher import FSMContext
import markups as nav
from dispatcher import dp


@dp.message_handler(lambda message: message.text == nav.btnMain, state="*")
async def back_to_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Back to menu", reply_markup=nav.mainMenu)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message, state: FSMContext):
    await message.reply(
        "Hello, it's a bot, which can send you <b>latest news</b>, <b>weather broadcats</b> and <b>exchange rates</b>!"
        "If you want to get some info about bot, type <b>/help<b>",
        parse_mode=types.ParseMode.HTML)
    await state.finish()
    await message.answer("What you want to choose?", reply_markup=nav.mainMenu)


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    """
    help handler
    """
    await message.answer(text=
                         "Basic functions of InfoBot: 📩\n"
                         "<b>Exchange Rates</b>: Returns information about <b>currency rate</b> 💵 or allow you to "
                         "exchange amount 📊\n"
                         "<b>Weather Broadcast</b>: Returns information about <b>current weather</b> according the "
                         "region you type 🌤, or give you forecast <b>by hours</b> 📅 \n"
                         "<b>Recent News</b>: Returns <b>10</b> last news from one of the most popular news source ⚡\n",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=nav.mainMenu)
