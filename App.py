import requests as rq
import json
from Pelicula import Pelicula
from Especie import Especie
import os

peliculas = []

def get_data():
    url = "https://www.swapi.tech/api/"
    response = rq.get(url)
    data = response.json()
    return data

def get_name_from_url(url):
    response = rq.get(url)
    data = response.json()
    return data['result']['properties']['name']

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

def get_species():
    url = "https://www.swapi.tech/api/species"
    response = rq.get(url)
    data = response.json()
    especies = []

    for especie in data['results']:
        especie_detail_url = especie['url']
        response_detail = rq.get(especie_detail_url)
        detail_data = response_detail.json()
        properties = detail_data['result']['properties']

        # Get homeworld name
        homeworld_name = get_name_from_url(properties['homeworld']) if properties['homeworld'] else 'Unknown'

        # Get names of people
        people_names = [get_name_from_url(person) for person in properties.get('people', [])]

        # Get names of films
        film_names = [get_name_from_url(film) for film in properties.get('films', [])]

        especie_obj = Especie(
            especie['name'],
            properties['average_height'],
            properties['classification'],
            homeworld_name,
            properties['language'],
            people_names,
            film_names
        )

        especies.append(especie_obj)

    return especies
def show_species():
    especies = get_species()
    for especie in especies:
        print(especie)

show_species()