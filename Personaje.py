class Personaje:
    def __init__(self, nombre, origen, peliculas, genero, especie, naves, vehiculos):
        self.nombre = nombre
        self.origen = origen
        self.peliculas = peliculas
        self.genero = genero
        self.especie = especie
        self.naves = naves
        self.vehiculos = vehiculos

    def __str__(self):
        return """---------Personaje---------
Nombre: {}
Origen: {}
Peliculas: {}
Genero: {}
Especie: {}
Naves: {}
Vehiculos: {}
--------------------------""".format(self.nombre, self.origen, self.peliculas, self.genero, self.especie, self.naves, self.vehiculos)
