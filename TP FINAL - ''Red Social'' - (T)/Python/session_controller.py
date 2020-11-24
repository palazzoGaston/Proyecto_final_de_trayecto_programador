# import
from usuario import Usuario
from cuenta import Cuenta
from login_account import Login
from dba import DataBase
from validador import Validador

# class
class SessionController():
    __usuario_activo = Usuario
    # cnstr
    def __init__(self, database=DataBase):
        self.__bd = database
        self.__log = Login(self.__bd)
        self.__vld = Validador(self.__bd)
    # mthds
    # gtt
    def get_usuario_activo(self):
        return self.__usuario_activo
    # stt
    def set_usuario_activo(self, nuevo_usuario_activo=Usuario):
        self.__usuario_activo = nuevo_usuario_activo
    # especificos
    def inciar_sesion(self):
        return self.__log.login_account() if not None else -1
    def menu_principal(self, cuenta_activa=Cuenta):
        cond = True
        while cond==True:
            print(f'\n\tMENU DE USUARIO'+
                '\n1. Ver datos'+
                '\n2. Modificar datos'+
                '\n3. Amigos'+
                '\n4. Posts'+
                '\n5. Eliminar cuenta'+
                '\n0. Cerrar sesion'
            )
            opc = input('\n<opcion>: ').lower()
            if opc == '0':
                cond = False
                print('\n[MENSAJE]: Sesion finalizada!')
            elif opc == '1':
                print(f'\n\tVER DATOS'+
                '\n1. Ver datos de cuenta'+
                '\n2. Ver datos de usuario'+
                '\n0. Atras')
                opc = input('\n<opcion>: ').strip()
                if opc == '0':
                    pass
                elif opc == '1':
                    cuenta_activa.mostrar_datos_de_cuenta()
                elif opc == '2':
                    cuenta_activa.get_usuario().mostrar_datos_de_usuario()
                else:
                    print('\n[Err]: opcion incorrecta!')
            elif opc == '2':
                print('\n\tMODIFICAR'+
                '\n1. Modificar datos de cuenta'+
                '\n2. Modificar datos de usuario'+
                '\n0. Atras')
                opc = input('\n<opcion>: ').strip()
                if opc == '0':
                    pass
                elif opc == '1':
                    # modificar datos de cuenta
                    print('\n\tMODIFICAR DATOS DE CUENTA'+
                    '\n1. Modificar login name'+
                    '\n2. Modificar login pass'+
                    '\n3. Modificar mail primario'+
                    '\n4. Modificar mail secundario'+
                    '\n0. Atras')
                    opc = input('\n<opcion>: ')
                    if opc == '0':
                        pass
                    elif opc == '1':
                        update_form = {'nuevo_login_name': input('\n<nuevo login_name>: ')}
                        cuenta_activa.update_acc(self.__vld, update_form)
                    elif opc == '2':
                        update_form = {'nuevo_login_pass': [input('\n<nuevo login_pass>: '), input('\n<nuevo login_pass_confirmacion>: ')]}
                        cuenta_activa.update_acc(self.__vld, update_form)
                    elif opc == '3':
                        update_form = {'nuevo_mail_primario': input('\n<nuevo mail_primario>: ')}
                        cuenta_activa.update_acc(self.__vld, update_form)
                    elif opc == '4':
                        update_form = {'nuevo_mail_secundario': input('\n<nuevo mail_secundario>: ')}
                        cuenta_activa.update_acc(self.__vld, update_form)
                    else:
                        print('\n[Err]: opcion incorrecta!')
                elif opc == '2':
                    # modificar datos de usuario
                    print('\n\tMODIFICAR DATOS DE USUARIO'+
                    '\n1. Modificar nombre'+
                    '\n2. Modificar apellido'+
                    '\n3. Modificar edad'+
                    '\n4. Modificar pais-ciudad'+
                    '\n5. Modificar genero'+
                    '\n6. Modificar telefono'+
                    '\n0. Atras')
                    opc = input('\n<opcion>: ')
                    if opc == '0':
                        pass
                    elif opc == '1':
                        update_form = {'nombre': input('\n<nuevo nombre>: ')}
                        cuenta_activa.get_usuario().update_user(self.__vld, update_form)
                    elif opc == '2':
                        update_form = {'apellido': input('\n<nuevo apellido>: ')}
                        cuenta_activa.get_usuario().update_user(self.__vld, update_form)
                    elif opc == '3':
                        update_form = {'edad': input('\n<nueva edad>: ')}
                        cuenta_activa.get_usuario().update_user(self.__vld, update_form)
                    elif opc == '4':
                        update_form = {
                            'pais': input('\n<nuevo pais>: '),
                            'ciudad': input('\n<nuevo ciudad>: ')
                        }
                        cuenta_activa.get_usuario().update_user(self.__vld, update_form)
                    elif opc == '5':
                        update_form = {'genero': input('\n<nuevo genero>: ')}
                        cuenta_activa.get_usuario().update_user(self.__vld, update_form)
                    elif opc == '6':
                        update_form = {'telefono': input('\n<nuevo telefono>: ')}
                        cuenta_activa.get_usuario().update_user(self.__vld, update_form)
                    else:
                        print('\n[Err]: opcion incorrecta!')
                else:
                    print('\n[Err]: opcion incorrecta!')
            elif opc == '3':
                print('\n\tAMIGOS'+
                '\n1. Agregar amigo'+
                '\n2. Ver lista de amigos'+
                '\n3. Eliminar amigo'+
                '\n4. Vaciar lista de amigos'+
                '\n0. Atras')
                opc = input('\n<opcion>: ').strip()
                if opc == '0':
                    pass
                elif opc == '1':
                    id_amigo = input('\n<amigo_id>: ')
                    cuenta_activa.agregar_amigo(id_amigo)
                elif opc == '2':
                    cuenta_activa.mostrar_lista_de_amigos()
                elif opc == '3':
                    id_amigo = input('\n<amigo_id>: ')
                    cuenta_activa.eliminar_amigo(id_amigo)
                elif opc == '4':
                    opc = input('\n[MENSAJE]: esta seguro que desea eliminar toda su lista de amigos?\n<s/n>: ').lower()
                    if opc == 's':
                        cuenta_activa.vaciar_lista_amigos()
                    elif opc == 'n':
                        print('\n[MENSAJE]: cambios descartados!')
                    else:
                        print('\n[Err]: opcion incorrecta!')
                else:
                    print('\n[Err]: opcion incorrecta!')
            elif opc == '4':
                print('\n\tPOSTS'+
                '\n1. Crear post'+
                '\n2. Ver mis post'+
                '\n3. Eliminar post'+
                '\n4. Eliminar todos mis post'+
                '\n0. Atras')
                opc = input('\n<opcion>: ').strip()
                if opc == '0':
                    pass
                elif opc == '1':
                    # crear publicacion
                    ctg = cuenta_activa.mostrar_categorias_de_publicacion()
                    print(f'\n*NOTA* -> Las categorias de post validas actualmente son: {ctg}')
                    body = input('\nContenido del post (max 300 caracteres): ')
                    categ = input('\nIngrese id de categoria del post: ').strip()
                    cuenta_activa.crear_publicacion(body, categ)
                elif opc == '2':
                    # ver publicaciones
                    cuenta_activa.mostrar_publicaciones()
                elif opc == '3':
                    # eliminar publicacion
                    id_post = input('<id_post>: ')
                    cuenta_activa.eliminar_publicacion(id_post)
                elif opc == '4':
                    # eliminar todas las publicaciones
                    opc = input('\n[MENSAJE]: esta seguro que desea eliminar todas sus publicaciones?\n<s/n>: ').lower()
                    if opc == 's':
                        cuenta_activa.eliminar_todas_las_publicaciones()
                    elif opc == 'n':
                        print('\n[MENSAJE]: cambios descartados!')
                    else:
                        print('\n[Err]: opcion incorrecta!')
                else:
                    print('\n[Err]: opcion incorrecta!')
            elif opc == '5':
                opc = input('\n[MENSAJE]: esta seguro que desea eliminar su cuenta?\n<s/n>: ').lower()
                if opc == 's':
                    cuenta_activa.eliminar_cuenta()
                    print('\n[MENSAJE]: Su cuenta ah sido eliminada!')
                    print('\n[MENSAJE]: Sesion finalizada!')
                    cond = False
                elif opc == 'n':
                    print('\n[MENSAJE]: cambios descartados!')
                else:
                    print('\n[Err]: opcion incorrecta!')
            else:
                print('\n[Err]: Opcion incorrecta!')