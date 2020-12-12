import sys
sys.path.append('../Practica')
from Menus.menu import Menu
from Menus.menu_modif_cuenta import MenuModificarDatosDeCuenta
from Menus.menu_modif_usuario import MenuModificarDatosDeUsuario

class MenuModificarDatos(Menu):
    
    # att
    __opciones = {}
    
    # cnstr
    def __init__(self, cuenta_activa, validador):
        super()
        self.__c_a = cuenta_activa
        self.__vld = validador
    
    # mthds

    # override
    def EjecutarOpcion(self, inpt):
        self.__opciones['1'] = MenuModificarDatosDeCuenta(self.__c_a, self.__vld)
        self.__opciones['2'] = MenuModificarDatosDeUsuario(self.__c_a, self.__vld)
        return self.__opciones[inpt]

    # override
    def MostrarOpciones(self):
        while True:
            print('\n\tMODIFICAR'+
                    '\n1. Modificar datos de cuenta'+
                    '\n2. Modificar datos de usuario'+
                    '\n0. Atras')
            
            inpt = input('\n<opcion>: ')
            
            if inpt == '0': break
            elif inpt in ['1', '2']: self.EjecutarOpcion(inpt).MostrarOpciones()
            else: print('\n[Err]: Opcion incorrecta!')