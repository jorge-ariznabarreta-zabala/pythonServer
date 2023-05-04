from flask import Flask, request
from .weather import get_city_by, get_all_cities, post_city


app = Flask(__name__)

@app.route("/cities/<city_id>", methods=['GET'])
def get_city(city_id):
    return get_city_by(city_id)

@app.route("/cities", methods=['GET'])
def get_cities():
    return get_all_cities()

@app.route("/cities", methods=["POST"])
def new_city():
    data= request.get_json()
    print ('**newcity', data['id'])
    post_city(data)
    return ""

@app.route("/")
def hello_root():
    return 'Hola'