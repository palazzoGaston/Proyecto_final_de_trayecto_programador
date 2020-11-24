# import
from datetime import datetime

# class
class Publicacion():
    # cnstr
    def __init__(self, id_de_publicacion=int, body=str, fecha_de_publicacion=str, categoria_de_publicacion=str, autor=int):
        self.__id_de_publicacion = id_de_publicacion
        self.__body = body
        self.__fecha_de_publicacion = fecha_de_publicacion
        self.__autor = autor
        self.__categoria_de_publicacion = categoria_de_publicacion
    # mthds
    # gtt
    def get_id_de_publicacion(self):
        return self.__id_de_publicacion
    def get_body(self):
        return self.__body
    def get_fecha_de_publicacion(self):
        return self.__fecha_de_publicacion
    def get_autor(self):
        return self.__autor
    def get_categoria_de_publicacion(self):
        return self.__categoria_de_publicacion
    # stt
    def set_body(self, new_body):
        self.__body = new_body
    def set_fecha_de_publicacion(self, new_fecha_de_publicacion):
        self.__fecha_de_publicacion = new_fecha_de_publicacion
    def set_autor(self, new_autor):
        self.__autor = new_autor
    def set_categoria_de_publicacion(self, new_categoria_de_publicacion):
        self.__categoria_de_publicacion = new_categoria_de_publicacion