class Pelicula:
    def __init__(self, titulo, numero_ep, fecha_estreno, opening_crawl, nombre_director):
        self.titulo = titulo
        self.numero_ep = numero_ep
        self.fecha_estreno = fecha_estreno
        self.opening_crawl = opening_crawl
        self.nombre_director = nombre_director

    def __str__(self):
        return """---------Pelicula---------
Titulo: {}
Numero Episodio: {}
Fecha de Estreno: {}
Opening Crawl: {}
Nombre del Director: {}
--------------------------""".format(self.titulo, self.numero_ep, self.fecha_estreno, self.opening_crawl, self.nombre_director)