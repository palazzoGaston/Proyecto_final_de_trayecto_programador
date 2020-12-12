# imports
import sys
sys.path.append('../Practica')
from Menus.menu import Menu

# class
class MenuVerDatos(Menu):
    
    # cnstr
    def __init__(self, cuenta_activa):
        super()
        self.__cuenta_activa = cuenta_activa
    
    # mthds

    # override
    def EjecutarOpcion(self, inpt):
        if inpt == '1': return self.__cuenta_activa.mostrar_datos_de_cuenta()
        elif inpt == '2': return self.__cuenta_activa.get_usuario().mostrar_datos_de_usuario()
        else: print('\n[Err]: Opcion incorrecta!')

    # override
    def MostrarOpciones(self):
        while True:
            print(f'\n\tVER DATOS'+
                    '\n1. Ver datos de cuenta'+
                    '\n2. Ver datos de usuario'+
                    '\n0. Atras'
                )
            
            inpt = input('\n<opcion>: ')
            
            if inpt == '0': break
            else: self.EjecutarOpcion(inpt)