from .weather_repository_sqlite import *

def get_city_by(city_id):
    return read(city_id)

def get_all_cities():
    return read_all()

def post_city(new_city):
    print(create(new_city))

def update_city(update_city):
    update(update_city)

def del_city(city_id):
    delete(city_id)
    
