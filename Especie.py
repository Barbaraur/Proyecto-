class Especie:
    def __init__(self, nombre, altura, clasificacion, planeta_origen, lengua_materna, nombre_personajes, nombre_episodios):
        self.nombre = nombre
        self.altura = altura
        self.clasificacion = clasificacion
        self.planeta_origen = planeta_origen
        self.lengua_materna = lengua_materna
        self.nombre_personajes = nombre_personajes
        self.nombre_episodios = nombre_episodios

    def __str__(self):
        return """---------Especie---------
Nombre: {}
Altura: {}
Clasificacion: {}
Planeta de Origen: {}
Lengua Materna: {}
Personajes: {}
Episodios: {}
--------------------------""".format(self.nombre, self.altura, self.clasificacion, self.planeta_origen, self.lengua_materna, self.nombre_personajes, self.nombre_episodios)