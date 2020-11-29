# import
from dba import DataBase

# class
class Usuario():
    bd = DataBase()
    # cnstr
    def __init__(self, user_id, nombre, apellido, edad, pais, ciudad, genero, tel):
        self.__user_id = user_id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__pais = pais
        self.__ciudad = ciudad
        self.__genero = genero
        self.__tel = tel
    # mthds
     # gtt
    def get_user_id(self):
        return self.__user_id
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_edad(self):
        return self.__edad
    def get_pais(self):
        return self.__pais
    def get_ciudad(self):
        return self.__ciudad
    def get_genero(self):
        return self.__genero
    def get_telefono(self):
        return self.__tel
    # stt
    def set_user_id(self, new_usuarios_id):
        self.__user_id = new_usuarios_id
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    def set_apellido(self, new_apellido):
        self.__apellido = new_apellido
    def set_edad(self, new_edad):
        self.__edad = new_edad
    def set_pais(self, new_pais):
        self.__pais = new_pais
    def set_ciudad(self, new_ciudad):
        self.__ciudad = new_ciudad
    def set_genero(self, new_genero):
        self.__genero = new_genero
    def set_tel(self, new_tel):
        self.__tel = new_tel
    # especificos
    def update_user(self, validador, update_form):
        vld = validador
        r, dic = vld.validar_datos_de_usuario(update_form)
        if r == 0:
            if 'nombre' in dic.keys():
                self.set_nombre(dic['nombre'])
            elif 'apellido' in dic.keys():
                self.set_apellido(dic['apellido'])
            elif 'edad' in dic.keys():
                self.set_edad(dic['edad'])
            elif 'ciudad' in dic.keys():
                qry = '''SELECT ciudades.nombre, paises.nombre
                FROM ciudades
                INNER JOIN paises ON (ciudades.pais_codigo = paises.codigo) AND (paises.id = %s)
                WHERE ciudad_id = %s;'''
                val = (dic['pais'], dic['ciudad'], )
                self.bd.get_cursor().execute(qry, val)
                r = self.bd.get_cursor().fetchall()
                self.set_pais(r[0][1])
                self.set_ciudad(r[0][0])
            elif 'genero' in dic.keys():
                self.set_genero(dic['genero'])
            elif 'telefono' in dic.keys():
                self.set_tel(dic['telefono'])
            # actualizando en bd
            pais_temp = self.get_pais()
            ciudad_temp = self.get_ciudad()
            qry = '''SELECT paises.id, ciudades.ciudad_id
            FROM paises
            INNER JOIN ciudades
            ON (paises.codigo = ciudades.pais_codigo)
            AND (ciudades.nombre = %s)
            WHERE paises.nombre = %s;'''
            val = (self.get_ciudad(), self.get_pais())
            self.bd.ejecutar(qry, val)
            r = self.bd.get_cursor().fetchall()
            self.set_pais(r[0][0])
            self.set_ciudad(r[0][1])
            self.save_user(auto=False)
            print('\n[MENSAJE]: informacion de usuario actualizada')
            # actualizando en tiempo de ejecucion
            self.set_pais(pais_temp)
            self.set_ciudad(ciudad_temp)
        else:
            print(f'\n[Err]: uno o mas datos no pudieron validarse ↓')
            for val in dic.values():
                for i in val:
                    print(f'\t{i}')
    def mostrar_datos_de_usuario(self):
        print(
            f'\n\tDatos de usuario'+
            f'\nID: {self.get_user_id()}'+
            f'\nNombre: {self.get_nombre()}'+
            f'\nApellido: {self.get_apellido()}'+
            f'\nEdad: {self.get_edad()}'+
            f'\nGenero: {self.get_genero()}'+
            f'\nTel: {self.get_telefono()}'+
            f'\nPais: {self.get_pais()}'+
            f'\nCiudad: {self.get_ciudad()}'
        )
    def save_user(self, auto=True):
        if auto:
            self.bd.actualizar_auto_increment('usuarios', 'usuarios_id')
        # value
        val = [
            self.get_user_id(),
            self.get_nombre(),
            self.get_apellido(),
            self.get_edad(),
            self.get_genero(),
            self.get_ciudad(),
            self.get_telefono()
        ]

        self.bd.get_cursor().callproc('save_user', val)
        self.bd.get_commit()
        for i in self.bd.get_cursor().stored_results():
            r = str(i.fetchone()[0])

        return r