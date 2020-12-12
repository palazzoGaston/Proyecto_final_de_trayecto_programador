import sys
sys.path.append('../Practica')
from Menus.menu import Menu

class MenuPosts(Menu):
    
    # att
    __opciones = {}

    # cnstr
    def __init__(self, cuenta_activa):
        super()
        self.__cuenta_activa = cuenta_activa
    
    # mthds
    def __CrearPost(self):
        ctg = self.__cuenta_activa.mostrar_categorias_de_publicacion()
        print(f'\n*NOTA* -> Las categorias de post validas actualmente son: {ctg}')
        body = input('\nContenido del post (max 300 caracteres): ')
        categ = input('\nIngrese id de categoria del post: ').strip()
        return self.__cuenta_activa.crear_publicacion(body, categ)
    def __VerMisPost(self):
        return self.__cuenta_activa.mostrar_publicaciones()
    def __EliminarPost(self):
        id_post = input('<id_post>: ')
        return self.__cuenta_activa.eliminar_publicacion(id_post)
    def __EliminarTodosMisPost(self):
        opc = input('\n[MENSAJE]: esta seguro que desea eliminar todas sus publicaciones?\n<s/n>: ').lower()
        if opc == 's':
            return self.__cuenta_activa.eliminar_todas_las_publicaciones()
        elif opc == 'n':
            return print('\n[MENSAJE]: cambios descartados!')

    # override
    def EjecutarOpcion(self, inpt):
        if inpt == '1': return self.__CrearPost()
        if inpt == '2': return self.__VerMisPost()
        if inpt == '3': return self.__EliminarPost()
        if inpt == '4': return self.__EliminarTodosMisPost()
        else: return print('\n[Err]: Opcion incorrecta!')

    # override
    def MostrarOpciones(self):
        while True:
            print('\n\tPOSTS'+
                '\n1. Crear post'+
                '\n2. Ver mis post'+
                '\n3. Eliminar post'+
                '\n4. Eliminar todos mis post'+
                '\n0. Atras'
                )
            
            inpt = input('\n<opcion>: ')
            
            if inpt == '0': break
            else: self.EjecutarOpcion(inpt)