import requests 

from config import *
    
def current_weather(q: str =  "Chicago", appid: str = APPID, units: str = "metric") -> dict:#текущяя погода
        data =  requests.get(URL_WEATHER+"weather", params=locals()).json()
        if data["cod"]=="404":
            return f'Ooops. Wrong city name. Try again'
        res = None
        for sub in data["weather"]:
            if sub["main"]:
                res = sub
                break
        return f'Location: {data["name"]} \nTemperature: {int(data["main"]["temp"])}  \nWeather status: {res["main"]}'

def weather_forecast(q: str = "Chicago", appid: str = APPID, units: str = "metric", cnt: str = "8") ->dict:#прогноз погоды
        data = requests.get(URL_WEATHER+"forecast", params=locals()).json()
        for item in data["list"]:
            value = data["list"]
        return "\n".join(list(map(str, value)))


