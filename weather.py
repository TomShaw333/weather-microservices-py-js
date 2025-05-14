import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def get_weather_data(city_name, state_code, country_code, Api_KEY):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={Api_KEY}').json()

    print(response)

print(get_weather_data('Vineland','NJ','US', api_key)  )  