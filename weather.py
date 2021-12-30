import requests 

from config import *

    
def current_weather(q: str =  "Chicago", appid: str = APPID, units: str = "metric") -> dict:#текущяя погода
        data =  requests.get(URL_BASE+"weather", params=locals()).json()
        res = None
        for sub in data["weather"]:
            if sub["main"]:
                res = sub
                break
        return f'Location: {data["name"]}  Temperature: {data["main"]["temp"]}  Weather status: {res["main"]}'

def weather_forecast(q: str = "Chicago", appid: str = APPID, units: str = "metric", cnt: str = "8") ->dict:#прогноз погоды
        data = requests.get(URL_BASE+"forecast", params=locals()).json()
        for item in data["list"]:
            value = data["list"]
        return "\n".join(list(map(str, value)))




if __name__ == "__main__":
    location = input("Enter a location: ").strip()

    print(weather_forecast(location))