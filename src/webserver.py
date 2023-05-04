from flask import Flask
from .weather import get_weather

app = Flask(__name__)

@app.route("/cities/BIO")
def hello_world():
    return get_weather()

@app.route("/")
def hello_root():
    return 'Hola'