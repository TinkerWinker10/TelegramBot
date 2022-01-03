from aiogram import types
from aiogram.dispatcher import FSMContext
import markups as nav
from dispatcher import dp


@dp.message_handler(lambda message: message.text == "❗️Main menu❗️", state="*")
async def back_to_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Back to menu", reply_markup=nav.mainMenu)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message, state: FSMContext):
    await message.reply(
        "Hello, it's a bot, which can send you <b>latest news</b>, <b>weather broadcats</b> and <b>exchange rates</b>!",
        parse_mode=types.ParseMode.HTML)
    await state.finish()
    await message.answer("What you want to choose?", reply_markup=nav.mainMenu)


@dp.message_handler(commands=['help'])
async def help_handler():
    """
    help handler
    """
    pass
