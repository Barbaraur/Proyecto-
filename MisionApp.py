import pandas as pd
from Mision import Mision

class MisionApp:
    def __init__(self):
        # Inicializa la clase MisionApp con listas y datos de CSV
        self.misiones = []
        self.planetas = pd.read_csv('starwars/csv/planets.csv')
        self.naves = pd.read_csv('starwars/csv/starships.csv')
        self.armas = pd.read_csv('starwars/csv/weapons.csv')
        self.personajes = pd.read_csv('starwars/csv/characters.csv')

    def agregar_mision(self, nombre, planeta_destino, nave, armas, miembros):
        # Agrega una misión a la lista de misiones
        if len(self.misiones) >= 5:
            print("No se pueden agregar más de 5 misiones.")
            return
        mission = Mision(nombre, planeta_destino, nave, armas, miembros)
        self.misiones.append(mission)

    def display_missions(self):
        # Muestra todas las misiones almacenadas
        for mission in self.misiones:
            print(mission)

    def get_planet_names(self):
        # Obtiene una lista de nombres de planetas
        return self.planetas['name'].tolist()

    def get_ship_names(self):
        # Obtiene una lista de nombres de naves
        return self.naves['name'].tolist()

    def get_weapon_names(self):
        # Obtiene una lista de nombres de armas
        return self.armas['name'].tolist()

    def get_character_names(self):
        # Obtiene una lista de nombres de personajes
        return self.personajes['name'].tolist()

    def construct_mission(self):
        # Construye una misión solicitando detalles al usuario
        print("Escribe los detalles de la misión")
        name = input("Escribe el nombre de la misión: ")
        print("Escoge el planeta de destino:")
        for planet in self.get_planet_names():
            print(f"{self.get_planet_names().index(planet) + 1}. {planet}")
        planet_choice = int(input("Escoge el número del planeta de destino: "))
        planet_destino = self.planetas.iloc[planet_choice - 1]['name']
        print("Escoge la nave:")
        for ship in self.get_ship_names():
            print(f"{self.get_ship_names().index(ship) + 1}. {ship}")
        ship_choice = int(input("Escoge el número de la nave: "))
        nave = self.naves.iloc[ship_choice - 1]['name']
        print("Escoge las armas:")
        for weapon in self.get_weapon_names():
            print(f"{self.get_weapon_names().index(weapon) + 1}. {weapon}")
        weapon_choice = input("Escoge los números de las armas a utilizar separados por comas con un máximo de 7: ")
        armas = []
        for choice in weapon_choice.split(','):
            armas.append(self.armas.iloc[int(choice) - 1]['name'])
        print("Escoge los miembros:")
        for character in self.get_character_names():
            print(f"{self.get_character_names().index(character) + 1}. {character}")
        character_choice = input("Escoge los números de los miembros a utilizar separados por comas con un máximo de 7: ")
        miembros = []
        for choice in character_choice.split(','):
            miembros.append(self.personajes.iloc[int(choice) - 1]['name'])
        self.agregar_mision(name, planet_destino, nave, armas, miembros)

    def modify_mission(self):
        # Modifica una misión existente
        if not self.misiones:
            print("No hay misiones disponibles")
            return

        print("Selecciona la misión a modificar:")
        for idx, mission in enumerate(self.misiones):
            print(f"{idx + 1}. {mission.nombre}")

        mission_choice = int(input("Escribe el número de la misión a modificar: ")) - 1
        if mission_choice < 0 or mission_choice >= len(self.misiones):
            print("Elección inválida.")
            return

        mission = self.misiones[mission_choice]
        print(f"Misión seleccionada: {mission}")

        print("¿Qué quieres modificar?: ")
        print("1. Nombre")
        print("2. Planeta")
        print("3. Nave")
        print("4. Armas")
        print("5. Personajes")
        attribute_choice = int(input("Escoge el número de la opción a modificar: "))

        if attribute_choice == 1:
            new_name = input("Escoge el nuevo nombre: ")
            mission.nombre = new_name
        elif attribute_choice == 2:
            print("Selecciona un nuevo planeta:")
            for idx, planet in enumerate(self.get_planet_names()):
                print(f"{idx + 1}. {planet}")
            planet_choice = int(input("Escoge el número del planeta a escoger")) - 1
            if planet_choice < 0 or planet_choice >= len(self.planetas):
                print("Opción inválida")
                return
            mission.planeta_destino = self.planetas.iloc[planet_choice]['name']
        elif attribute_choice == 3:
            print("Selecciona una nueva nave:")
            for idx, ship in enumerate(self.get_ship_names()):
                print(f"{idx + 1}. {ship}")
            ship_choice = int(input("Selecciona el número de tu nueva nave: ")) - 1
            if ship_choice < 0 or ship_choice >= len(self.naves):
                print("Opción inválida.")
                return
            mission.nave = self.naves.iloc[ship_choice]['name']
        elif attribute_choice == 4:
            print("Modificar armas:")
            print("1. Agregar arma")
            print("2. Eliminar arma")
            weapon_mod_choice = int(input("Elige tu opción:"))
            if weapon_mod_choice == 1:
                print("Selecciona las armas a agregar:")
                for idx, weapon in enumerate(self.get_weapon_names()):
                    print(f"{idx + 1}. {weapon}")
                weapon_choice = int(input("Selecciona los números de las armas a escoger: ")) - 1
                if weapon_choice < 0 or weapon_choice >= len(self.armas):
                    print("Opción inválida")
                    return
                mission.armas.append(self.armas.iloc[weapon_choice]['name'])
            elif weapon_mod_choice == 2:
                print("Escoge las armas a eliminar:")
                for idx, weapon in enumerate(mission.armas):
                    print(f"{idx + 1}. {weapon}")
                weapon_choice = int(input("Escoge los números de las armas a eliminar: ")) - 1
                if weapon_choice < 0 or weapon_choice >= len(mission.armas):
                    print("Opción inválida.")
                    return
                mission.armas.pop(weapon_choice)
        elif attribute_choice == 5:
            print("Modificar miembros:")
            print("1. Agregar miembro")
            print("2. Remover miembro")
            member_mod_choice = int(input("Selecciona tu opción: "))
            if member_mod_choice == 1:
                print("Selecciona el miembro a agregar:")
                for idx, character in enumerate(self.get_character_names()):
                    print(f"{idx + 1}. {character}")
                member_choice = int(input("Escoge el número del personaje a agregar: ")) - 1
                if member_choice < 0 or member_choice >= len(self.personajes):
                    print("Opción inválida.")
                    return
                mission.miembros.append(self.personajes.iloc[member_choice]['name'])
            elif member_mod_choice == 2:
                print("Selecciona el miembro a remover:")
                for idx, member in enumerate(mission.miembros):
                    print(f"{idx + 1}. {member}")
                member_choice = int(input("Selecciona el número del personaje a eliminar: ")) - 1
                if member_choice < 0 or member_choice >= len(mission.miembros):
                    print("Opción inválida.")
                    return
                mission.miembros.pop(member_choice)
        else:
            print("Opción inválida.")
            return

        print("Misión modificada exitosamente.")

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
                file.write("\n")  # Agregar una nueva línea entre misiones

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
        # Ejecuta el menú de la aplicación
        while True:
            print("1. Agregar Misión")
            print("2. Mostrar Misiones")
            print("3. Modificar Misiones")
            print("4. Cargar misiones")
            print("5. Salir y guardar misiones")
            choice = int(input("Coloca tu opción: "))
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
                print("Saliendo del menú.")
                break
            else:
                print("Opción inválida.")