# imports
from abc import ABC, abstractmethod

# class
class Menu(ABC):
    # cnstr
    def __init__(self, cuenta_activa):
        self.__opciones = {}
        self.__index = 0
    
    # methds
    def get_opciones(self):
        return self.__opciones
    def get_index(self):
        return self.__index

    def Agregar(self, menu=object):
        self.__opciones[str(self.__index)] = menu
        self.__index+=1
    
    @abstractmethod
    def MostrarOpciones(self):
        pass
    @abstractmethod
    def EjecutarOpcion(self):
        pass