import sys
sys.path.append('../Practica')
from Menus.menu import Menu

class MenuModificarDatosDeCuenta(Menu):

    # att
    __opciones = {}

    # cnstr
    def __init__(self, cuenta_activa, validador):
        super()
        self.__cuenta_activa = cuenta_activa
        self.__vld = validador
    
    # mthds
    def __ModificarLoginName(self):
        update_form = {'nuevo_login_name': input('\n<nuevo login_name>: ')}
        return self.__cuenta_activa.update_acc(self.__vld, update_form)
    def __ModificarLoginPass(self):
        update_form = {'nuevo_login_pass': [input('\n<nuevo login_pass>: '), input('\n<nuevo login_pass_confirmacion>: ')]}
        return self.__cuenta_activa.update_acc(self.__vld, update_form)
    def __ModificarMailPrimario(self):
        update_form = {'nuevo_mail_primario': input('\n<nuevo mail_primario>: ')}
        return self.__cuenta_activa.update_acc(self.__vld, update_form)
    def __ModificarMailSecundario(self):
        update_form = {'nuevo_mail_secundario': input('\n<nuevo mail_secundario>: ')}
        return self.__cuenta_activa.update_acc(self.__vld, update_form)

    # override
    def EjecutarOpcion(self, inpt):
        if inpt == '1': return self.__ModificarLoginName()
        elif inpt == '2': return self.__ModificarLoginPass()
        elif inpt == '3': return self.__ModificarMailPrimario()
        elif inpt == '4': return self.__ModificarMailSecundario()
        else: return print('\n[Err]: Opcion incorrecta!')

    # override
    def MostrarOpciones(self):
        while True:
            print('\n\tMODIFICAR DATOS DE CUENTA'+
                '\n1. Modificar login name'+
                '\n2. Modificar login pass'+
                '\n3. Modificar mail primario'+
                '\n4. Modificar mail secundario'+
                '\n0. Atras'
            )
            
            inpt = input('\n<opcion>: ')
            
            if inpt == '0': break
            else: self.EjecutarOpcion(inpt)