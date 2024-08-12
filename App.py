import requests as rq
from Pelicula import Pelicula
from Especie import Especie
from Planeta import Planeta
from Personaje import Personaje

peliculas = []
especies = []
planetas = []
personajes = []

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
    return data['result']

def show_films():
    for pelicula in peliculas:
        print(pelicula)

def get_species(films_data):
    url = "https://www.swapi.tech/api/species"
    response = rq.get(url)
    data = response.json()

    species_films = {species['url']: [] for species in data['results']}

    for film in films_data:
        for species_url in film['properties']['species']:
            if species_url in species_films:
                species_films[species_url].append(film['properties']['title'])

    for especie in data['results']:
        especie_detail_url = especie['url']
        response_detail = rq.get(especie_detail_url)
        detail_data = response_detail.json()
        properties = detail_data['result']['properties']

        homeworld_name = get_name_from_url(properties['homeworld']) if properties['homeworld'] else 'Unknown'
        people_names = [get_name_from_url(person) for person in properties.get('people', [])]
        film_names = species_films[especie_detail_url]

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

    return data['results']

def show_species():
    for especie in especies:
        print(especie)

def get_planets(films_data):
    url = "https://www.swapi.tech/api/planets"
    response = rq.get(url)
    data = response.json()

    planet_films = {planet['url']: [] for planet in data['results']}
    planet_residents = {planet['url']: [] for planet in data['results']}

    for film in films_data:
        for planet_url in film['properties']['planets']:
            if planet_url in planet_films:
                planet_films[planet_url].append(film['properties']['title'])

    people_url = "https://www.swapi.tech/api/people"
    response_people = rq.get(people_url)
    people_data = response_people.json()

    for person in people_data['results']:
        person_detail_url = person['url']
        response_person_detail = rq.get(person_detail_url)
        person_detail_data = response_person_detail.json()
        person_properties = person_detail_data['result']['properties']

        homeworld_url = person_properties['homeworld']
        if homeworld_url in planet_residents:
            planet_residents[homeworld_url].append(person_properties['name'])

    for planeta in data['results']:
        planeta_detail_url = planeta['url']
        response2 = rq.get(planeta_detail_url)
        detail_data = response2.json()
        properties = detail_data['result']['properties']

        films = planet_films[planeta_detail_url]
        residents = planet_residents[planeta_detail_url]

        planeta_obj = Planeta(
            properties['name'],
            properties['orbital_period'],
            properties['rotation_period'],
            properties['population'],
            properties['climate'],
            films,
            residents
        )

        planetas.append(planeta_obj)

def show_planets():
    for planeta in planetas:
        print(planeta)

def get_characters(films_data):
    url = "https://www.swapi.tech/api/people"
    response = rq.get(url)
    data = response.json()

    character_films = {character['url']: [] for character in data['results']}
    character_species = {character['url']: [] for character in data['results']}
    character_starships = {character['url']: [] for character in data['results']}
    character_vehicles = {character['url']: [] for character in data['results']}

    for film in films_data:
        for character_url in film['properties']['characters']:
            if character_url in character_films:
                character_films[character_url].append(film['properties']['title'])

    species_url = "https://www.swapi.tech/api/species"
    response_species = rq.get(species_url)
    species_data = response_species.json()

    species_character_map = {}
    for species in species_data['results']:
        species_detail_url = species['url']
        response_detail = rq.get(species_detail_url)
        detail_data = response_detail.json()
        properties = detail_data['result']['properties']
        for character_url in properties.get('people', []):
            species_character_map[character_url] = properties['name']

    starships_url = "https://www.swapi.tech/api/starships"
    response_starships = rq.get(starships_url)
    starships_data = response_starships.json()

    for starship in starships_data['results']:
        starship_detail_url = starship['url']
        response_starship_detail = rq.get(starship_detail_url)
        starship_detail_data = response_starship_detail.json()
        starship_properties = starship_detail_data['result']['properties']

        for pilot_url in starship_properties['pilots']:
            if pilot_url in character_starships:
                character_starships[pilot_url].append(starship_properties['name'])

    vehicles_url = "https://www.swapi.tech/api/vehicles"
    response_vehicles = rq.get(vehicles_url)
    vehicles_data = response_vehicles.json()

    for vehicle in vehicles_data['results']:
        vehicle_detail_url = vehicle['url']
        response_vehicle_detail = rq.get(vehicle_detail_url)
        vehicle_detail_data = response_vehicle_detail.json()
        vehicle_properties = vehicle_detail_data['result']['properties']

        for pilot_url in vehicle_properties['pilots']:
            if pilot_url in character_vehicles:
                character_vehicles[pilot_url].append(vehicle_properties['name'])

    for person in data['results']:
        person_detail_url = person['url']
        response_person_detail = rq.get(person_detail_url)
        person_detail_data = response_person_detail.json()
        person_properties = person_detail_data['result']['properties']

        homeworld_name = get_name_from_url(person_properties['homeworld']) if person_properties['homeworld'] else 'Unknown'
        films = character_films[person_detail_url]
        species = species_character_map.get(person_detail_url, 'Unknown')
        starships = character_starships[person_detail_url]
        vehicles = character_vehicles[person_detail_url]

        personaje = Personaje(
            person_properties['name'],
            homeworld_name,
            films,
            person_properties['gender'],
            species,
            starships,
            vehicles
        )

        personajes.append(personaje)

def search_character():
    name = input("Busqueda del personaje: ")
    results = [personaje for personaje in personajes if name.lower() in personaje.nombre.lower()]
    for personaje in results:
        print(personaje)

if __name__ == "__main__":
    films_data = get_films()
    species_data = get_species(films_data)
    get_planets(films_data)
    get_characters(films_data)
    search_character()