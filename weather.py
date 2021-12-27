import requests 
from pprint import pprint
from config import *


class Weather:
    def __init__(self, units = "metric"):
        self.units = units

    
    def current_weather(self, q: str =  "Chicago", appid: str = APPID) -> dict:#текущяя погода
        data =  requests.get(URL_BASE+"weather", params=locals()).json()
        print(URL_BASE)
        return data
  

    def weather_forecast(self, q: str = "Chicago", appid: str = APPID) ->dict:#прогноз погоды
        data = requests.get(URL_BASE+"forecast", params=locals()).json()
        return data


    def weather_onecall(self, lat: float = 55.68, lon: float = 12.57, appid: str = APPID) -> dict:#json по локации
        data = requests.get(URL_BASE+"onecall", params=locals()).json()
        return data



if __name__ == "__main__":
    x = Weather("metric")
    location = input("Enter a location: ").strip()
    pprint(x.weather_forecast(location))
