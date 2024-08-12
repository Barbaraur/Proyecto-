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

    def construct_mission(self):
        print("Escribe los detalles de la mision")
        name = input("Escribe el nombre de la mision: ")
        print("Escoge el planeta de destino:")
        for planet in self.get_planet_names():

            print(f"{self.get_planet_names().index(planet) + 1}. {planet}")
        planet_choice = int(input("Escoge el numero del planeta de destino: "))
        planet_destino = self.planetas.iloc[planet_choice - 1]['name']
        print("Escoge la nave:")
        for ship in self.get_ship_names():

            print(f"{self.get_ship_names().index(ship) + 1}. {ship}")
        ship_choice = int(input("Escoge el numero de la nave: "))
        nave = self.naves.iloc[ship_choice - 1]['name']
        print("Escoge las armas:")
        for weapon in self.get_weapon_names():

            print(f"{self.get_weapon_names().index(weapon) + 1}. {weapon}")
        weapon_choice = input("Escoge los numeros de las armas a utilizar separados por comas con un maximo de 7: ")
        armas = []
        for choice in weapon_choice.split(','):
            armas.append(self.armas.iloc[int(choice) - 1]['name'])
        print("Escoge los miembros:")
        for character in self.get_character_names():

            print(f"{self.get_character_names().index(character) + 1}. {character}")
        character_choice = input("Escoge los numeros de los miembros a utilizar separados por comas con un maximo de 7: ")
        miembros = []
        for choice in character_choice.split(','):
            miembros.append(self.personajes.iloc[int(choice) - 1]['name'])
        self.agregar_mision(name, planet_destino, nave, armas, miembros)


    def run(self):
        while True:
            print("1. Add a mission")
            print("2. Display missions")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.construct_mission()
            elif choice == 2:
                self.display_missions()
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")
        print("Exiting the program.")
        return

if __name__ == '__main__':
    app = MisionApp()
    app.run()


