from typing import Tuple,Optional
import datetime

__cache = {}
life_time_hours = 1.0

def get_weather(city:str , state:Optional[str],country:str,units:str)->Optional[dict]:
    key = __create_key(city,state,country,units)  # creating key which is reusable for encrypting and decrypting
    data:dict = __cache.get(key)
    if not data:
        return None
    # Determine last time when data came into dictionary 
    last = data['time']
    dt = datetime.datetime.now() - last
    if dt/datetime.timedelta(minutes=60)<life_time_hours: # If data is present since less than hour in cache then good to go and return data value
        return data['value']
    del __cache[key]
    return None

def set_weather(city:str,state:str,country:str,units:str,value:str):
    key = __create_key(city,state,country,units)
    data = {'time':datetime.datetime.now(),'value':value}
    __cache[key] = data
    __clear_out_of_date()

def __create_key(city:str,state:str,country:str,units:str)->Tuple[str,str,str,str]:
    if not city or not country or not units:
        raise Exception("City,country and units are required")
    if not state:
        state = ''
    return city.strip().lower(),state.strip().lower(),country.strip().lower(),units.strip().lower()

def __clear_out_of_date():
    # Delete cache data if it persists > life_time_hours
    for key,data in __cache.items():
        dt = datetime.datetime.now() - data.get('time')
        if dt/datetime.timedelta(minutes=60) > life_time_hours:
            del __cache[key]



