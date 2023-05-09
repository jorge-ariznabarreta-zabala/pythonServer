WEATHER_DB={
    'BIO':{
        "id": "BIO",
        "name": "Bilbao",
        "temperature": 30,
        "rain_probability": 0.5
    },
    'RMA':{
        "id": "RMA",
        "name": "Roma",
        "temperature": 25,
        "rain_probability": 0.3
    },
}
def get_city_by(city_id):
    return WEATHER_DB.get(city_id)

def get_all_cities():
    return WEATHER_DB

def post_city(new_city): 
     WEATHER_DB[new_city['id']] = new_city

def patch_city(update_city): 
    print ('***update en weather')
    WEATHER_DB[update_city['id']] = update_city

def del_city(city_id): 
    print ('***del en weather')
    return WEATHER_DB.pop(city_id)