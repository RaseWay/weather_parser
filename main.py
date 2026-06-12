class CityWeather:
    def __init__(self, name: str, temperature: float, condition: str, wind_speed: float):
        self.name = name
        self.temperature = temperature
        self.condition = condition
        self.wind_speed = wind_speed

    def __str__(self):
        return f"В городе {self.name} сейчас {self.temperature}*C, на улице: {self.condition}. Скорость ветра на улице: {self.wind_speed}"