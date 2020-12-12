import sys
sys.path.append('../Practica')
from Menus.menu import Menu

class MenuModificarDatosDeUsuario(Menu):
    # att
    __opciones = {}
    # cnstr
    def __init__(self, cuenta_activa, validador):
        super()
        self.__cuenta_activa = cuenta_activa
        self.__vld = validador
    
    # mthds
    def __ModificarNombre(self):
        update_form = {'nombre': input('\n<nuevo nombre>: ')}
        return self.__cuenta_activa.get_usuario().update_user(self.__vld, update_form)
    def __ModificarApellido(self):
        update_form = {'apellido': input('\n<nuevo apellido>: ')}
        return self.__cuenta_activa.get_usuario().update_user(self.__vld, update_form)
    def __ModificarEdad(self):
        update_form = {'edad': input('\n<nueva edad>: ')}
        return self.__cuenta_activa.get_usuario().update_user(self.__vld, update_form)
    def __ModificarPaisCiudad(self):
        update_form = {
            'pais': input('\n<nuevo pais>: '),
            'ciudad': input('\n<nuevo ciudad>: ')
        }
        return self.__cuenta_activa.get_usuario().update_user(self.__vld, update_form)
    def __ModificarGenero(self):
        update_form = {'genero': input('\n<nuevo genero>: ')}
        return self.__cuenta_activa.get_usuario().update_user(self.__vld, update_form)
    def __ModificarTelefono(self):
        update_form = {'telefono': input('\n<nuevo telefono>: ')}
        return self.__cuenta_activa.get_usuario().update_user(self.__vld, update_form)

    # override
    def EjecutarOpcion(self, inpt):
        if inpt == '1': return self.__ModificarNombre()
        elif inpt == '2': return self.__ModificarApellido()
        elif inpt == '3': return self.__ModificarEdad()
        elif inpt == '4': return self.__ModificarPaisCiudad()
        elif inpt == '5': return self.__ModificarGenero()
        elif inpt == '6': return self.__ModificarTelefono()
        else: return print('\n[Err]: Opcion incorrecta!')

    # override
    def MostrarOpciones(self):
        while True:
            print('\n\tMODIFICAR DATOS DE USUARIO'+
                '\n1. Modificar nombre'+
                '\n2. Modificar apellido'+
                '\n3. Modificar edad'+
                '\n4. Modificar pais-ciudad'+
                '\n5. Modificar genero'+
                '\n6. Modificar telefono'+
                '\n0. Atras'
            )
            
            inpt = input('\n<opcion>: ')
            
            if inpt == '0': break
            else: self.EjecutarOpcion(inpt)