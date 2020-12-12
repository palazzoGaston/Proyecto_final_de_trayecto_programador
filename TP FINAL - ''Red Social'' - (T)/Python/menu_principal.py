# import
from Menus.menu import Menu
from Menus.menu_ver_datos import MenuVerDatos
from Menus.menu_modificar_datos import MenuModificarDatos
from Menus.menu_amigos import MenuAmigos
from Menus.menu_posts import MenuPosts
from Menus.menu_eliminar_cuenta import MenuEliminarCuenta

# class
class MenuPrincipal(Menu):
    
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
        if inpt == '1': return MenuVerDatos(self.__c_a)
        elif inpt == '2': return MenuModificarDatos(self.__c_a, self.__vld)
        elif inpt == '3': return MenuAmigos(self.__c_a)
        elif inpt == '4': return MenuPosts(self.__c_a)
        elif inpt == '5': return MenuEliminarCuenta(self.__c_a)
        else: print('\n[Err]: Opcion incorrecta!')

    # override
    def MostrarOpciones(self):
        while True:
            print(f'\n\tMENU DE PRINCIPAL'+
                    '\n1. Ver datos'+
                    '\n2. Modificar datos'+
                    '\n3. Amigos'+
                    '\n4. Posts'+
                    '\n5. Eliminar cuenta'+
                    '\n0. Cerrar sesion'
                )
            
            inpt = input('\n<opcion>: ')
            
            if inpt == '0': break
            elif inpt in ['1', '2', '3', '4', '5']:
                if self.EjecutarOpcion(inpt).MostrarOpciones() == -1: break
            else: print('\n[Err]: Opcion incorrecta!')