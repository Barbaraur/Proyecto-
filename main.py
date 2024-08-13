from MisionApp import MisionApp
from App import menuApp
from Appcsv import menuAppCsv

def menu_principal():
    while True:
        print("1. Menu de API")
        print("2. Menu de CSV")
        print("3. Menu de Misiones")
        print("4. Salir")

        option = input("Seleccione una opcion: ")
        while option not in ['1', '2', '3', '4']:
            option = input("Seleccione una opcion valida: ")

        if option == '1':
            menuApp()
        elif option == '2':
            menuAppCsv()
        elif option == '3':
            mision_app = MisionApp()
            mision_app.run()
        elif option == '4':
            print("Saliendo del menu principal")
            exit()

menu_principal()
