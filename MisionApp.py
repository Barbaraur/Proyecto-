import pandas as pd
from Mision import Mision


class MisionApp:
    def __init__(self):

        self.misiones = []
        self.planetas = pd.read_csv('starwars/csv/planets.csv')
        self.naves = pd.read_csv('starwars/csv/starships.csv')
        self.armas = pd.read_csv('starwars/csv/weapons.csv')
        self.personajes = pd.read_csv('starwars/csv/characters.csv')

    def agregar_mision(self, nombre, planeta_destino, nave, armas, miembros):
        if len(self.misiones) >= 5:
            print("Cannot add more than 5 missions.")
            return
        mission = Mision(nombre , planeta_destino, nave, armas, miembros)
        self.misiones.append(mission)

    def display_missions(self):
        for mission in self.misiones:
            print(mission)

    def get_planet_names(self):
        return self.planetas['name'].tolist()

    def get_ship_names(self):
        return self.naves['name'].tolist()

    def get_weapon_names(self):
        return self.armas['name'].tolist()

    def get_character_names(self):
        return self.personajes['name'].tolist()