import requests
from config import URL_WEATHER, APPID


def current_weather(q: str = "Chicago", appid: str = APPID, units: str = "metric") -> str:  # текущяя погода
    data = requests.get(URL_WEATHER + "weather", params=locals()).json()
    if data["cod"] == "404":
        return f'Ooops. Wrong city name. Try again'
    res = None
    for sub in data["weather"]:
        if sub["main"]:
            res = sub
            break
    return f'Location: {data["name"]} \nTemperature: {int(data["main"]["temp"])}  \nWeather status: {res["main"]}'


def weather_forecast(q: str = "Chicago", appid: str = APPID, units: str = "metric",
                     cnt: str = "8") -> str:  # прогноз погоды
    data = requests.get(URL_WEATHER + "forecast", params=locals()).json()
    if data["cod"] == "404":
        return f'Ooops. Wrong city name. Try again'
    value = data["list"]
    return "\n".join(
        list(map(str, [f'Time: {item["dt_txt"]} Temperature:{int(item["main"]["temp"])}' for item in value])))


