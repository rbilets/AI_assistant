import requests, json

from datetime import datetime


def get_weather(city_name):
    api_key = "e4b910b230d252e819ff6c0c59e9586d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url).text
    data = json.loads(response)

    temperature = int(data['main']['temp'] - 273.15)
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    rise = datetime.fromtimestamp(data['sys']['sunrise']).strftime("%I:%M %p")
    set = datetime.fromtimestamp(data['sys']['sunset']).strftime("%I:%M %p")

    return description, temperature, humidity, rise, set
