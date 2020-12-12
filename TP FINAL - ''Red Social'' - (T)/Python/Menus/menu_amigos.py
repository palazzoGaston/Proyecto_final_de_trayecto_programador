import sys
sys.path.append('../Practica')
from Menus.menu import Menu

class MenuAmigos(Menu):
    
    # cnstr
    def __init__(self, cuenta_activa):
        super()
        self.__cuenta_activa = cuenta_activa
    
    # mthds
    def __AgregarAmigo(self):
        id_amigo = input('\n<amigo_id>: ')
        return self.__cuenta_activa.agregar_amigo(id_amigo)
    def __VerListaDeAmigos(self):
        return self.__cuenta_activa.mostrar_lista_de_amigos()
    def __EliminarAmigo(self):
        id_amigo = input('\n<amigo_id>: ')
        return self.__cuenta_activa.eliminar_amigo(id_amigo)
    def __VaciarListaDeAmigos(self):
        opc = input('\n[MENSAJE]: esta seguro que desea eliminar toda su lista de amigos?\t<s/n>: ').lower()
        if opc == 's':
            return self.__cuenta_activa.vaciar_lista_amigos()
        elif opc == 'n':
            print('\n[MENSAJE]: cambios descartados!')
    
    # override
    def EjecutarOpcion(self, inpt):
        if inpt == '1': return self.__AgregarAmigo()
        elif inpt == '2': return self.__VerListaDeAmigos()
        elif inpt == '3': return self.__EliminarAmigo()
        elif inpt == '4': return self.__VaciarListaDeAmigos()
        else: return print('\n[Err]: Opcion incorrecta!')
    
    # override
    def MostrarOpciones(self):
        while True:
            print('\n\tAMIGOS'+
                '\n1. Agregar amigo'+
                '\n2. Ver lista de amigos'+
                '\n3. Eliminar amigo'+
                '\n4. Vaciar lista de amigos'+
                '\n0. Atras'
            )
            
            inpt = input('\n<opcion>: ')
            
            if inpt == '0': break
            else: self.EjecutarOpcion(inpt)