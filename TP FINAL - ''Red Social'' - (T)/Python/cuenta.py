# import
from publicacion import Publicacion
from usuario import Usuario
from dba import DataBase
import base64

# class
class Cuenta():
    # cnst
    def __init__(self, cuenta_id, login_name, login_pass, usuario, mail_primario, mail_secundario, database):
        self.__bd = database
        self.__cuenta_id = cuenta_id
        self.__login_name = login_name
        self.__login_pass = self.__encriptarPass(login_pass)
        self.__usuario = usuario
        self.__mail_primario = mail_primario
        self.__mail_secundario = mail_secundario
        self.__publicaciones = []
        self.__amistades = []
    #mthds
    # gtt
    def get_cuenta_id(self):
        return self.__cuenta_id
    def get_login_name(self):
        return self.__login_name
    def get_login_pass(self):
        return self.__desencriptarPass(self.__login_pass)
    def get_usuario(self):
        return self.__usuario
    def get_mail_primario(self):
        return self.__mail_primario
    def get_mail_secundario(self):
        return self.__mail_secundario
    def get_publicaciones(self):
        return self.__publicaciones
    def get_amistades(self):
        return self.__amistades
    # stt
    def set_cuenta_id(self, new_id):
        self.__cuenta_id = new_id
    def set_login_name(self, new_login_name):
        self.__login_name = new_login_name
    def set_login_pass(self, new_pass):
       self.__login_pass = self.__encriptarPass(new_pass)
    def set_usuario(self, new_usuario):
        self.__usuario = new_usuario
    def set_mail_primario(self, new_mail_primario):
        self.__mail_primario = new_mail_primario
    def set_mail_secundario(self, new_mail_secundario):
        self.__mail_secundario = new_mail_secundario
    def set_publicaciones(self, new_publicaciones):
        self.__publicaciones.append(new_publicaciones)
    def set_amistades(self, new_amistades):
        self.__amistades = new_amistades
    # especificos
    def update_acc(self, validador, update_form):
        vld = validador
        for key, val in update_form.items():
            if val != '':
                # validacion
                if key == 'nuevo_login_name':
                    r, dic = vld.validar_registro({'login_name': val})
                elif key == 'nuevo_login_pass':
                    r, dic = vld.validar_registro({'login_pass': val})
                elif key == 'nuevo_mail_primario':
                    r, dic = vld.validar_registro({'mail_primario': val})
                elif key == 'nuevo_mail_secundario':
                    r, dic = vld.validar_registro({'mail_secundario': val})
                # actualizacion
                if r == 0:
                    if key == 'nuevo_login_name':
                        self.set_login_name(dic['login_name'])
                    elif key == 'nuevo_login_pass':
                        self.set_login_pass(dic['login_pass'])
                    elif key == 'nuevo_mail_primario':
                        self.set_mail_primario(dic['mail_primario'])
                    elif key == 'nuevo_mail_secundario':
                        self.set_mail_secundario(dic['mail_secundario'])
                    self.save_account(auto=False)
                    print('\n[MENSAJE]: informacion de cuenta actualizada')
                else:
                    print(f'\n[Err]: uno o mas datos no pudieron validarse ↓')
                    for val in dic.values():
                        if type(val).__name__ not in ['DataBase']:
                            for i in val:
                                print(f'\t{i}')
            else:
                print('\n[MENSAJE]: no se realizo ningun cambio')
    def mostrar_lista_de_amigos(self):
        qry = '''SELECT CONCAT(usuarios.nombre, " ", usuarios.apellido), usuarios.usuarios_id
        FROM amistades
        INNER JOIN usuarios ON amistades.usuario_id_amigo = usuarios.usuarios_id
        WHERE amistades.usuario_id_1 = %s;'''
        val = (self.get_usuario().get_user_id(), )
        self.__bd.ejecutar(qry, val)
        r = self.__bd.get_cursor().fetchall()
        if r != []:
            print('\n\tLISTA DE AMIGOS')
            print('\nUsuario\t\t|\tID\n')
            for amigos in r:
                print(f'{amigos[0]}\t\t{amigos[1]}')
        else:
            print('\n[MENSAJE]: tu lista de amigos se encuentra vacia actualmente')
    def mostrar_categorias_de_publicacion(self):
        qry = 'select categoriasdepost_id, nombre from categoriasdepost;'
        self.__bd.get_cursor().execute(qry)
        r = self.__bd.get_cursor().fetchall()
        if r != []:
            cadena = ''
            for i in r:
                if r.index(i) == 0:
                    cadena += f' {i[0]}-{i[1]}'
                else:
                    cadena += f', {i[0]}-{i[1]}'
        return cadena
    def mostrar_publicaciones(self):
        self.cargar_publicaciones()
        for i in self.get_publicaciones():
            print(f'\nposteo_id: {i.get_id_de_publicacion()}'+
            f'\ncontenido: {i.get_body()}'+
            f'\nfecha_de_publ: {i.get_fecha_de_publicacion()}'+
            f'\ncategoria: {i.get_categoria_de_publicacion()}'+
            f'\nautor: {i.get_autor()}')
    def cargar_publicaciones(self):
        qry = '''SELECT posteos.posteos_id, posteos.contenido, posteos.fechaDePublicacion, categoriasdepost.nombre, cuentas.login_name
        FROM posteos
        INNER JOIN categoriasdepost ON posteos.categoriaDePost_id = categoriasdepost.CategoriasDePost_id
        INNER JOIN usuarios ON posteos.usuario_id_2 = usuarios.usuarios_id
        INNER JOIN cuentas ON usuarios.usuarios_id = cuentas.usuario_id_2
        WHERE posteos.usuario_id_2 = %s;'''
        val = (self.get_usuario().get_user_id(), )
        self.__bd.ejecutar(qry, val)
        r = self.__bd.get_cursor().fetchall()
        if r != []:
            for p in r:
                self.set_publicaciones(Publicacion(*p))
        else:
            return print('\n[MENSAJE]: su lista de posts esta actualmente vacia')
    def vaciar_lista_amigos(self):
        val = [self.get_usuario().get_user_id()]
        self.__bd.get_cursor().callproc('eliminar_todas_las_amistades', val)
        self.__bd.get_commit()
        for i in self.__bd.get_cursor().stored_results():
            print(f'\n[MENSAJE]: {i.fetchone()[0]}')
    def eliminar_amigo(self, amigo_id):
        val = [self.get_usuario().get_user_id(), amigo_id]
        self.__bd.get_cursor().callproc('eliminar_amigo', val)
        self.__bd.get_commit()
        for i in self.__bd.get_cursor().stored_results():
            print(f'\n[MENSAJE]: {i.fetchone()[0]}')
    def agregar_amigo(self, amigo_id):
        if amigo_id != str(self.get_usuario().get_user_id()):
            self.__bd.actualizar_auto_increment('amistades', 'amistades_id')
            val = [self.get_usuario().get_user_id(), amigo_id]
            self.__bd.get_cursor().callproc('agregar_amigo', val)
            self.__bd.get_commit()
            for i in self.__bd.get_cursor().stored_results():
                print(f'\n[MENSAJE]: {i.fetchone()[0]}')
        else:
            print('\n[Err]: no puedes agregarte a ti mismo como amigo!')
    def eliminar_todas_las_publicaciones(self):
        val = [self.get_usuario().get_user_id()]
        self.__bd.get_cursor().callproc('eliminar_todas_las_publicaciones', val)
        self.__bd.get_commit()
        for i in self.__bd.get_cursor().stored_results():
            print(f'\n[MENSAJE]: {i.fetchone()[0]}')
    def eliminar_publicacion(self, id_de_publicacion):
        val = [self.get_usuario().get_user_id(), id_de_publicacion]
        self.__bd.get_cursor().callproc('eliminar_amigo', val)
        self.__bd.get_commit()
        for i in self.__bd.get_cursor().stored_results():
            print(f'\n[MENSAJE]: {i.fetchone()[0]}')
    def crear_publicacion(self, contenido, categoria_id):
        self.__bd.actualizar_auto_increment('posteos', 'posteos_id')
        val = [self.get_usuario().get_user_id(), contenido, categoria_id]
        self.__bd.get_cursor().callproc('agregar_publicacion', val)
        self.__bd.get_commit()
        for i in self.__bd.get_cursor().stored_results():
            print(f'\n[MENSAJE]: {i.fetchone()[0]}')
    def mostrar_datos_de_cuenta(self):
        print(f'\n\tDatos de Cuenta'+
            f'\nID: {self.get_cuenta_id()}'+
            f'\nLogin: {self.get_login_name()}'+
            f'\nPass: {self.get_login_pass()}'+
            f'\nMail primario: {self.get_mail_primario()}'+
            f'\nMail secundario: {self.get_mail_secundario()}'
        )
    def eliminar_cuenta(self):
        val = [self.get_usuario().get_user_id()]
        self.__bd.get_cursor().callproc('eliminar_cuenta', val)
        self.__bd.get_commit()
    def __encriptarPass(self, password_a_encriptar=str):
        b = password_a_encriptar.encode("UTF-8") # codificacion a bytes
        e = base64.b64encode(b) # coodificacion a base64
        return e
    def __desencriptarPass(self, password_a_desencriptar):
        b = base64.b64decode(password_a_desencriptar)
        s = b.decode("UTF-8")
        return s
    def save_account(self, auto=True):
        if auto:
            self.__bd.actualizar_auto_increment('cuentas', 'cuenta_id')
        # value
        val = [
            self.get_cuenta_id(),
            self.get_login_name(),
            self.__encriptarPass(self.get_login_pass()),
            self.get_usuario().get_user_id(),
            self.get_mail_primario(),
            self.get_mail_secundario()
        ]
        self.__bd.get_cursor().callproc('save_acc', val)
        self.__bd.get_commit()
        for i in self.__bd.get_cursor().stored_results():
            r = str(i.fetchone()[0])
        return r