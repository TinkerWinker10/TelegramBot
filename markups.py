from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Main menu')


# -- Menu -- 
btnExchange = KeyboardButton('Exchange Rates')
btnWeather = KeyboardButton('Weather Broadcasts')
btnNews = KeyboardButton('Recent News')
mainMenu  = ReplyKeyboardMarkup(resize_keyboard=True).add(btnExchange, btnWeather, btnNews)

# -- Exchange --
btnInfo = KeyboardButton('Info')
btnRate = KeyboardButton('Exchange')
exhangeMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnRate, btnMain)

# -- Weather --
btnWeatherInfo = KeyboardButton('Weather Info')
btnCurrent = KeyboardButton('Current Weather')
btnForecast = KeyboardButton('Weather Forecast')
weatherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnWeatherInfo, btnCurrent, btnForecast, btnMain)

# ** Forecast MENU **
forecastMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)


# ** Current Weather MENU **
currentWeatherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)

# -- News -- 

