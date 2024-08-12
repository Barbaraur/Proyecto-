class Planeta:
    def __init__(self, nombre, periodo_orbita, periodo_rotacion, cantidad_residentes, tipo_clima, lista_episodios, lista_personajes):
        self.nombre = nombre
        self.periodo_orbita = periodo_orbita
        self.periodo_rotacion = periodo_rotacion
        self.cantidad_residentes = cantidad_residentes
        self.tipo_clima = tipo_clima
        self.lista_episodios = lista_episodios
        self.lista_personajes = lista_personajes

    def __str__(self):
        return """---------Planeta---------
Nombre: {}
Periodo de Orbita: {}
Periodo de Rotacion: {}
Cantidad de Residentes: {}
Tipo de Clima: {}
Episodios: {}
Personajes: {}
--------------------------""".format(self.nombre, self.periodo_orbita, self.periodo_rotacion, self.cantidad_residentes, self.tipo_clima, self.lista_episodios, self.lista_personajes)
