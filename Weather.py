import requests
import math


city_name = 'Safi'
api_key= 'c5848cdd34b1a2fcff47b5558f728fee'
def get_weather_current(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url).json()

    temp = response['main']['temp']
    #temp = math.floor(temp  - 273.15)  # Convert to °F

    feels_like = response['main']['feels_like']
    #feels_like = math.floor(feels_like - 273.15)  # Convert to °F

    humidity = response['main']['humidity']

    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }

weather = get_weather_current(api_key, city_name)

print(weather)