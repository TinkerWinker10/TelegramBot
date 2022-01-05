from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton('❗️Main menu❗️')
# -- Menu --
btnExchange = KeyboardButton('💶Exchange Rates💶')
btnWeather = KeyboardButton('☀️Weather Broadcast☀️')
btnNews = KeyboardButton('🌐Recent News🌐')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnExchange, btnWeather, btnNews)


# -- Exchange --
btnCurrencyRate = KeyboardButton('💸Currency Rate💸')
btnExchangeAmount = KeyboardButton('💰Exchange Amount💰')
exchangeMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCurrencyRate, btnExchangeAmount, btnMain)


# -- Weather --
btnCurrent = KeyboardButton('⛈Current Weather⛈')
btnForecast = KeyboardButton('🌪Weather Forecast🌪')
weatherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCurrent, btnForecast, btnMain)

# ** Forecast MENU **
forecastMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)

# ** Current Weather MENU **
currentWeatherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)

# -- News --
btnTribuna = KeyboardButton("🥇Tribuna🥇")
btnTSN = KeyboardButton("📍TSN📍")
btnUnian = KeyboardButton("📍UNIAN📍")
btnBBC = KeyboardButton("🗞BBC🗞")
btnSport = KeyboardButton("⚽️Sport.ua⚽️")
newsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTribuna, btnTSN, btnUnian, btnBBC, btnSport, btnMain)
