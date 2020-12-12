import sys
sys.path.append('../Practica')
from Menus.menu import Menu

class MenuEliminarCuenta(Menu):
    
    # cnstr
    def __init__(self, cuenta_activa):
        super()
        self.__cuenta_activa = cuenta_activa
    
    # mthds

     # override
    def EjecutarOpcion(self, inpt=None):
        opc = input('\n[MENSAJE]: esta seguro que desea eliminar su cuenta?\t<s/n>: ').lower()
        if opc == 's':
            self.__cuenta_activa.eliminar_cuenta()
            print('\n[MENSAJE]: Su cuenta ah sido eliminada!')
            print('\n[MENSAJE]: Sesion finalizada!')
            return False
        elif opc == 'n':
            print('\n[MENSAJE]: cambios descartados!')
            return False
        else: 
            return print('\n[Err]: Opcion incorrecta!')

    # override
    def MostrarOpciones(self):
        while True: 
            if self.EjecutarOpcion() is False: break