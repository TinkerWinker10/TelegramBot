from aiogram import types
import markups as nav
from dispatcher import dp
from news import *


@dp.message_handler(lambda message: message.text == nav.btnTribuna)
async def tribuna_news(message: types.Message):
    await message.answer(get_tribuna_news())


@dp.message_handler(lambda message: message.text == nav.btnTSN)
async def tsn_news(message: types.Message):
    await message.answer(get_tsn_news())


@dp.message_handler(lambda message: message.text == nav.btnUnian)
async def unian_news(message: types.Message):
    await message.answer(get_unian_news())


@dp.message_handler(lambda message: message.text == nav.btnBBC)
async def bbc_news(message: types.Message):
    await message.answer(get_bbc_news())


@dp.message_handler(lambda message: message.text == nav.btnSport)
async def sport_news(message: types.Message):
    await message.answer(get_sport_news())





