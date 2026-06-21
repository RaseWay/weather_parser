import requests

class CityWeather:
    def __init__(self, name: str, temperature: float, condition: str, wind_speed: float):
        self.name = name
        self.temperature = temperature
        self.condition = condition
        self.wind_speed = wind_speed

    def __str__(self):
        return f"В городе {self.name} сейчас {self.temperature}*C, на улице: {self.condition}. Скорость ветра на улице: {self.wind_speed} метра в секунду"

API_KEY = "f1b99a75e2a74a0882690228262106"
CITY = "Tyumen"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&lang=ru"

response = requests.get(url)
data = response.json()

city_name = data["location"]["name"]
temperature = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]
wind_speed_ms = round(data["current"]["wind_kph"]/3.6, 1)

current_weather = CityWeather(
    name=city_name,
    temperature=temperature,
    condition=condition,
    wind_speed=wind_speed_ms
)

print(current_weather)