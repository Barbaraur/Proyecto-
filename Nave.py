class Nave:
    def __init__(self, modelo, longitud, capacidad_carga, hiperimpulsor, velmax, costo_creds):
        self.modelo = modelo
        self.longitud = longitud
        self.capacidad_carga = capacidad_carga
        self.hiperimpulsor = hiperimpulsor
        self.velmax = velmax
        self.costo_creds = costo_creds

    def __str__(self):
        return """---------Nave---------
Modelo: {}
Longitud: {}
Capacidad de Carga: {}
Hiperimpulsor: {}
Velocidad Maxima: {}
Costo en Creditos: {}
--------------------------""".format(self.modelo, self.longitud, self.capacidad_carga, self.hiperimpulsor, self.velmax, self.costo_creds)



