class Mision:
    def __init__(self, nombre, planeta_destino, nave, armas, miembros):
        self.nombre = nombre
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = armas
        self.miembros = miembros


    def __str__(self):
        return """---------Mision---------
Nombre: {}
Planeta de Destino: {}
Nave: {}
Armas: {}
Miembros: {}
--------------------------""".format(self.nombre, self.planeta_destino, self.nave, self.armas, self.miembros)