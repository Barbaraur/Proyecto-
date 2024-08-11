import requests as rq
import json
from Pelicula import Pelicula
import os

peliculas = []

def get_data():
    url = "https://www.swapi.tech/api/"
    response = rq.get(url)
    data = response.json()
    return data

def get_films():
    url = "https://www.swapi.tech/api/films"
    response = rq.get(url)
    data = response.json()
    for film in data['result']:
        pelicula = Pelicula(film['properties']['title'], film['properties']['episode_id'], film['properties']['release_date'], film['properties']['opening_crawl'], film['properties']['director'])
        peliculas.append(pelicula)

def show_films():
    for pelicula in peliculas:
        print(pelicula)

get_films()
show_films()

