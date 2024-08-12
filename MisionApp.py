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
        mission = Mision(nombre, planeta_destino, nave, armas, miembros)
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

    def modify_mission(self):
        if not self.misiones:
            print("No hay misiones disponibles")
            return

        print("Selecciona la mision a modificar:")
        for idx, mission in enumerate(self.misiones):
            print(f"{idx + 1}. {mission.nombre}")

        mission_choice = int(input("Escribe el numero de la mision a modificar: ")) - 1
        if mission_choice < 0 or mission_choice >= len(self.misiones):
            print("Invalid choice.")
            return

        mission = self.misiones[mission_choice]
        print(f"Mision seleccionada: {mission}")

        print("Que quieres modificar: ")
        print("1. Nombre")
        print("2. Planeta")
        print("3. Nave")
        print("4. Armas")
        print("5. Personajes")
        attribute_choice = int(input("Escoge el numero de la opcion a modificar: "))

        if attribute_choice == 1:
            new_name = input("Escoge el nuevo nombre: ")
            mission.nombre = new_name
        elif attribute_choice == 2:
            print("Selecciona un nuevo planeta:")
            for idx, planet in enumerate(self.get_planet_names()):
                print(f"{idx + 1}. {planet}")
            planet_choice = int(input("Escoge el numero del planeta a escoger")) - 1
            if planet_choice < 0 or planet_choice >= len(self.planetas):
                print("Opcion invalida")
                return
            mission.planeta_destino = self.planetas.iloc[planet_choice]['name']
        elif attribute_choice == 3:
            print("Select a new ship:")
            for idx, ship in enumerate(self.get_ship_names()):
                print(f"{idx + 1}. {ship}")
            ship_choice = int(input("Selecciona el numero de tu nueva nave: ")) - 1
            if ship_choice < 0 or ship_choice >= len(self.naves):
                print("Opcion invalida.")
                return
            mission.nave = self.naves.iloc[ship_choice]['name']
        elif attribute_choice == 4:
            print("Modificar armas:")
            print("1. Agregar arma")
            print("2. Eliminar arma")
            weapon_mod_choice = int(input("Elige tu opcion:"))
            if weapon_mod_choice == 1:
                print("Selecciona las armas a agregar:")
                for idx, weapon in enumerate(self.get_weapon_names()):
                    print(f"{idx + 1}. {weapon}")
                weapon_choice = int(input("Selecciona los numeros de las armas a escoger: ")) - 1
                if weapon_choice < 0 or weapon_choice >= len(self.armas):
                    print("Opcion invalida")
                    return
                mission.armas.append(self.armas.iloc[weapon_choice]['name'])
            elif weapon_mod_choice == 2:
                print("Escoge las armas a eliminar:")
                for idx, weapon in enumerate(mission.armas):
                    print(f"{idx + 1}. {weapon}")
                weapon_choice = int(input("Escoge los numeros de las armas a eliminar: ")) - 1
                if weapon_choice < 0 or weapon_choice >= len(mission.armas):
                    print("Opcion invalida.")
                    return
                mission.armas.pop(weapon_choice)
        elif attribute_choice == 5:
            print("Modify members:")
            print("1. Agregar miembro")
            print("2. Remover miembro")
            member_mod_choice = int(input("Selecciona tu opcion: "))
            if member_mod_choice == 1:
                print("Selecciona el miembro a agregar:")
                for idx, character in enumerate(self.get_character_names()):
                    print(f"{idx + 1}. {character}")
                member_choice = int(input("Escoge el numero del personaje a agregar: ")) - 1
                if member_choice < 0 or member_choice >= len(self.personajes):
                    print("Opcion invalida.")
                    return
                mission.miembros.append(self.personajes.iloc[member_choice]['name'])
            elif member_mod_choice == 2:
                print("Selecciona el miembro a remover:")
                for idx, member in enumerate(mission.miembros):
                    print(f"{idx + 1}. {member}")
                member_choice = int(input("Selecciona el numero del personaje a eliminar: ")) - 1
                if member_choice < 0 or member_choice >= len(mission.miembros):
                    print("Opcion invalida.")
                    return
                mission.miembros.pop(member_choice)
        else:
            print("Opcion invalida.")
            return

        print("Mision modificada exitosamente.")

    def save_mission_data(mission_data, file_name):
        """
        Guardar misiones en un archivo de texto.

        :param mission_data: Lista de misiones a guardar.
        :param file_name: Nombre del archivo para guardar los datos.
        """
        with open(file_name, 'w') as file:
            for mission in mission_data:
                mission_dict = {
                    'Nombre': mission.nombre,
                    'Planeta de Destino': mission.planeta_destino,
                    'Nave': mission.nave,
                    'Armas': ', '.join(mission.armas),
                    'Miembros': ', '.join(mission.miembros)
                }
                for key, value in mission_dict.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")  # Add a newline between missions

    def load_mission_data(self, file_name):
        """
        Cargar misiones desde un archivo de texto.

        :param file_name: Nombre del archivo para cargar los datos.
        """
        with open(file_name, 'r') as file:
            mission_data = file.read().split('\n\n')
            for mission_str in mission_data:
                if mission_str.strip():
                    mission_dict = {}
                    for line in mission_str.split('\n'):
                        key, value = line.split(': ', 1)
                        mission_dict[key] = value
                    self.agregar_mision(
                        mission_dict['Nombre'],
                        mission_dict['Planeta de Destino'],
                        mission_dict['Nave'],
                        mission_dict['Armas'].split(', '),
                        mission_dict['Miembros'].split(', ')
                    )

    def run(self):
        while True:
            print("1. Agregar Mision")
            print("2. Mostrar Misiones")
            print("3. Modificar Misiones")
            print("4. Cargar misiones")
            print("5. Salir y guardar misiones")
            choice = int(input("Coloca tu opcion: "))
            if choice == 1:
                self.construct_mission()
            elif choice == 2:
                self.display_missions()
            elif choice == 3:
                self.modify_mission()
            elif choice == 4:
                self.load_mission_data('mission_data.txt')
            elif choice == 5:
                MisionApp.save_mission_data(self.misiones, 'mission_data.txt')
                break
            else:
                print("Opcion invalida.")
        print("Saliendo del programa.")
        return

if __name__ == '__main__':
    app = MisionApp()
    app.run()