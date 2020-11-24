# import
import base64
from dba import DataBase
from usuario import Usuario
from cuenta import Cuenta
from validador import Validador

# class
class Login():
    # cnstr
    def __init__(self, database=DataBase):
        self.__mydb = database
        self.__vld = Validador(self.__mydb)
    # methds
    def __desencriptarPass(self, password_a_desencriptar):
        b = base64.b64decode(password_a_desencriptar)
        s = b.decode("UTF-8")
        return s
    def __encriptarPass(self, password_a_encriptar=str):
        b = password_a_encriptar.encode("UTF-8") # codificacion a bytes
        e = base64.b64encode(b) # coodificacion a base64
        return e
    def login_account(self):
        print('\nPantalla de logeo ↓')
        # query ↓
        sql = '''SELECT usuarios_id, usuarios.nombre, apellido, edad, paises.nombre AS "pais", ciudades.nombre AS "ciudad", genero, telefono
        FROM usuarios
        INNER JOIN ciudades ON ciudad_id_1 = ciudades.ciudad_id
        INNER JOIN paises ON ciudades.pais_codigo = paises.codigo
        INNER JOIN cuentas ON usuarios.usuarios_id = cuentas.usuario_id_2
        WHERE login_name = %s AND login_pass = %s;'''
        # values ↓
        form_login = {
            'login_name' : input('\n<login_name>: '),
            'login_pass' : input('\n<login_pass>: ')
        }
        r, dic = self.__vld.validar_login(form_login)
        if r == 0:
            dic['login_pass'] = str(self.__encriptarPass(dic['login_pass'])).split("'")[1]
            val = (dic['login_name'], dic['login_pass'], )
            self.__mydb.ejecutar(sql, val)
            rows = self.__mydb.get_cursor().fetchall()
            if len(rows) > 0 :
                nw_user = Usuario(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6], rows[0][7])
                # query ↓
                sql = 'SELECT * FROM cuentas WHERE usuario_id_2 = %s;'
                # value ↓
                val = (nw_user.get_user_id(), )
                self.__mydb.ejecutar(sql, val)
                rows = self.__mydb.get_cursor().fetchall()
                nw_acc = Cuenta(rows[0][0], rows[0][1], self.__desencriptarPass(rows[0][2]), nw_user, rows[0][4], rows[0][5], self.__mydb)
                return nw_acc
            else:
                print(f'\n[Err]: nombre de usuario o contraseña incorrectos!')
                return None
        else:
            print(f'\n[Err]: uno o mas datos no pudieron validarse ↓')
            for val in dic.values():
                print(f'\t{val[0]}')
            return None