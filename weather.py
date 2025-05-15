import requests
#from dotenv import load_dotenv
#import os

#load_dotenv()
#api_key = os.getenv('API_KEY')

#Example output JSON
#{'coord': {'lon': -75.0257, 'lat': 39.4862}, 'weather': 
# [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 
# 'base': 'stations', 'main': {'temp': 290.97, 'feels_like': 291.34, 'temp_min': 290.27, 
# 'temp_max': 291.49, 'pressure': 1013, 'humidity': 97, 'sea_level': 1013, 'grnd_level': 1009}, 
# 'visibility': 10000, 'wind': {'speed': 2.28, 'deg': 108, 'gust': 3.36}, 'clouds': {'all': 86}, 
# 'dt': 1747283531, 'sys': {'type': 2, 'id': 39390, 'country': 'US', 'sunrise': 1747302361, 'sunset': 1747354024}, 
# 'timezone': -14400, 'id': 4504621, 'name': 'Vineland', 'cod': 200}

def get_weather_data_city_state_country(city_name, state_code, country_code, API_KEY):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_KEY}').json()

    #print(response)
    return response

#print(get_weather_data('vineland','nj','us', api_key)  )  


def get_weather_data_city_country(city_name, country_code, API_KEY):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}').json()

    return response

#print(get_weather_data('vineland','nj','us', api_key)  )  

def get_weather_data_city_only(city_name, API_KEY):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}').json()

    return response
