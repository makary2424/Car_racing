import json
from time import sleep
import requests

KEY_API = '6e7cdffb5003fc399996236f2a2d822c'
GEOCODER_API = '25e218c5-01e9-4b8c-8006-b87976d6f9e3'


def select_cities():
    print('Введите название города, чтобы добавить, или хватит, чтобы закончить')
    locations = dict()
    while True:
        city = input('Введите город: ')
        if city.lower() == 'хватит':
            break
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={KEY_API}'
        data = json.loads(requests.get(url).text)[0]
        locations[city] = (data['lat'], data['lon'])
    return locations


def get_weather(places):
    weather = dict()
    for place in places:
        l1, l2 = places[place]
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={l1}&lon={l2}&appid={KEY_API}'
        data = json.loads(requests.get(url, params={'units': 'metric', 'lang': 'ru'}).text)
        weather[place] = {'temperature': data['main']['temp'], 'feels_like': data['main']['feels_like'],
                          'description': data['weather'][0]['description'], 'wind_speed': data['wind']['speed']}
    return weather


def print_info(weather):
    for key in weather:
        city = weather[key]
        print(
            f"{key.upper()}\nТемпература: {city['temperature']}\nОщущается как: {city['feels_like']}\n"
            f"Описание: {city['description']}\nСкорость ветра: {city['wind_speed']}")
        print('-' * 10)


print_info(get_weather(select_cities()))
