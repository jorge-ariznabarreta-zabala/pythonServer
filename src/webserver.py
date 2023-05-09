from flask import Flask, request
from .weather import *


app = Flask(__name__)

@app.route("/") #Si me pides /
def hello_root():
    return '<h1>Hola</h1>'

@app.route("/cities", methods=['GET'])#Si me pides /cities con GET
def get_cities():
    return get_all_cities()

@app.route("/cities/<city_id>", methods=['GET']) #Si me pides /cities/ALGO con GET
def get_city(city_id):
    return get_city_by(city_id)

@app.route("/cities", methods=["POST"]) #Si me pides /cities con POST
def new_city():
    data= request.get_json()
    print ('**newcity', data['id'])
    post_city(data)
    return ""

@app.route("/cities/<city_id>", methods=["PUT"])#Si me pides /cities/ALGO con PUT
def update_city(city_id):
    data= request.get_json()
    print ('**update_city', data['id'])
    patch_city(data)
    return ""

@app.route("/cities/<city_id>", methods=['DELETE'])#Si me pides /cities/ALGO con DELETE
def delete_(city_id):
    return del_city(city_id)