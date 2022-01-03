from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
