import os

import requests

from flask import Flask

from flask import request

app = Flask(__name__)


@app.route("/")
def index():

    # Etsy: https://api.etsy.com/v2/listings/active.js?api_key=cdwxq4soa7q4zuavbtynj8wx&keywords=bicycle&includes=Images,Shop&sort_on=score

    response = requests.get('https://swapi.co/api/planets')
    data = response.json()

    planets = data['results']

    planet_html = []
 #To access the key in the dictionary specify the name in print(planet['name'])
    for planet in planets:
        planet_html.append('<li>{} :: {}</li>'.format(planet['name'], planet['climate']))

    planet_html = ''.join(planet_html)


    #Gets html and render to screen
    index_file = open('index.html', 'r')
    index_html = index_file.read()

    #This replaces 'planet_list' with planet_html
    index_html = index_html.replace('{{planet_list}}', planet_html)

    index_file.close()

    return index_html



