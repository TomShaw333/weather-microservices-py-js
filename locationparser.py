import weather
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
#(city, state, country, [api])
#tolower
#cities must be given to call api
#states may or may not be given
#countries may or may not be given

def parse_city(city):
    #TODO exclude numbers. delete whitespace
    return city.lower()

def parse_state(state):
    #TODO exclude numbers. delete whitespace
    return state.lower()

def parse_country(country):
    #TODO exclude numbers. delete whitespace
    return country.lower()


def parse_input(city,state,country):
    if not city:
        print('Error: Invalid city string.')
        return None
    else:
        city_entered = True
        city_param = parse_city(city)
        
    if not state:
        state_entered = False
    else:
        state_entered = True        
        state_param = parse_state(state)

    if not country:
        country_entered = False
    else:
        country_entered = True
        country_param = parse_country(country)    

    if city_entered and state_entered and country_entered:
        print(weather.get_weather_data_city_state_country(city_param, state_param, country_param, api_key))    
    elif city_entered and country_entered:
        print(weather.get_weather_data_city_country(city_param, country_param, api_key))   
    elif city_entered:
        print(weather.get_weather_data_city_only(city_param, api_key))
    else:
        print('Unaccounted for city state country boolean configuration.')        


        
