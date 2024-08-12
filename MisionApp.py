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
            #Enumerando e imprimiendo para poder seleccionar del indice
            print(f"{self.get_planet_names().index(planet) + 1}. {planet}")
        planet_choice = int(input("Escoge el numero del planeta de destino: "))
        planet_destino = self.planetas.iloc[planet_choice - 1]['name']
        print("Escoge la nave:")
        for ship in self.get_ship_names():
            #Enumerando e imprimiendo para poder seleccionar del indice
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

    def modify_mission(self):
        if not self.misiones:
            print("No missions available to modify.")
            return

        print("Select a mission to modify:")
        for idx, mission in enumerate(self.misiones):
            print(f"{idx + 1}. {mission.nombre}")

        mission_choice = int(input("Enter the number of the mission to modify: ")) - 1
        if mission_choice < 0 or mission_choice >= len(self.misiones):
            print("Invalid choice.")
            return

        mission = self.misiones[mission_choice]
        print(f"Selected Mission: {mission}")

        print("What would you like to modify?")
        print("1. Name")
        print("2. Planet")
        print("3. Ship")
        print("4. Weapons")
        print("5. Members")
        attribute_choice = int(input("Enter your choice: "))

        if attribute_choice == 1:
            new_name = input("Enter the new name: ")
            mission.nombre = new_name
        elif attribute_choice == 2:
            print("Select a new planet:")
            for idx, planet in enumerate(self.get_planet_names()):
                print(f"{idx + 1}. {planet}")
            planet_choice = int(input("Enter the number of the new planet: ")) - 1
            if planet_choice < 0 or planet_choice >= len(self.planetas):
                print("Invalid choice.")
                return
            mission.planeta_destino = self.planetas.iloc[planet_choice]['name']
        elif attribute_choice == 3:
            print("Select a new ship:")
            for idx, ship in enumerate(self.get_ship_names()):
                print(f"{idx + 1}. {ship}")
            ship_choice = int(input("Enter the number of the new ship: ")) - 1
            if ship_choice < 0 or ship_choice >= len(self.naves):
                print("Invalid choice.")
                return
            mission.nave = self.naves.iloc[ship_choice]['name']
        elif attribute_choice == 4:
            print("Modify weapons:")
            print("1. Add weapon")
            print("2. Remove weapon")
            weapon_mod_choice = int(input("Enter your choice: "))
            if weapon_mod_choice == 1:
                print("Select a weapon to add:")
                for idx, weapon in enumerate(self.get_weapon_names()):
                    print(f"{idx + 1}. {weapon}")
                weapon_choice = int(input("Enter the number of the weapon to add: ")) - 1
                if weapon_choice < 0 or weapon_choice >= len(self.armas):
                    print("Invalid choice.")
                    return
                mission.armas.append(self.armas.iloc[weapon_choice]['name'])
            elif weapon_mod_choice == 2:
                print("Select a weapon to remove:")
                for idx, weapon in enumerate(mission.armas):
                    print(f"{idx + 1}. {weapon}")
                weapon_choice = int(input("Enter the number of the weapon to remove: ")) - 1
                if weapon_choice < 0 or weapon_choice >= len(mission.armas):
                    print("Invalid choice.")
                    return
                mission.armas.pop(weapon_choice)
        elif attribute_choice == 5:
            print("Modify members:")
            print("1. Add member")
            print("2. Remove member")
            member_mod_choice = int(input("Enter your choice: "))
            if member_mod_choice == 1:
                print("Select a member to add:")
                for idx, character in enumerate(self.get_character_names()):
                    print(f"{idx + 1}. {character}")
                member_choice = int(input("Enter the number of the member to add: ")) - 1
                if member_choice < 0 or member_choice >= len(self.personajes):
                    print("Invalid choice.")
                    return
                mission.miembros.append(self.personajes.iloc[member_choice]['name'])
            elif member_mod_choice == 2:
                print("Select a member to remove:")
                for idx, member in enumerate(mission.miembros):
                    print(f"{idx + 1}. {member}")
                member_choice = int(input("Enter the number of the member to remove: ")) - 1
                if member_choice < 0 or member_choice >= len(mission.miembros):
                    print("Invalid choice.")
                    return
                mission.miembros.pop(member_choice)
        else:
            print("Invalid choice.")
            return

        print("Mission modified successfully.")


    def run(self):
        while True:
            print("1. Add a mission")
            print("2. Display missions")
            print("3. Modify a mission")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.construct_mission()
            elif choice == 2:
                self.display_missions()
            elif choice == 3:
                self.modify_mission()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
        print("Exiting the program.")
        return

app = MisionApp()
app.run()


