# Get data from OpenweatherAPI and generate report #
from typing import Optional
import httpx
import os 
import json
from infrastructure import weather_cache
file_name = 'settings.json'
f = open(file_name)
file = json.load(f)
api_key = file.get('api_key')

async def get_weather_report(city:str , state:Optional[str]  , country:str , units:str)->dict:
    # Caching 
    # If there is data in cache , return it
    forecast =  weather_cache.get_weather(city,state,country,units)
    if forecast:
        return forecast
    

    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}"
    async with httpx.AsyncClient() as client:
        data = await client.get(url)
        data.raise_for_status()
    data = data.json()
    forecast = data['main']
    weather_cache.set_weather(city,state,country,units,forecast)
    print(forecast)
    return forecast


