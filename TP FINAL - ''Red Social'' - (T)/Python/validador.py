# import
from dba import DataBase

# class
class Validador():
    # cnstr
    def __init__(self, data_base=DataBase):
        self.__mydb = data_base
    # mthds
    def validar_mail(self, val):
        err = []
        count = 0
        dominios_validos = ['hotmail.com', 'gmail.com']
        if '@' in val:
            for dom in dominios_validos:
                if dom in val:
                    count+=1
            if count == 0:
                err.append('[Err]: los dominios contemplados como validos actulamente son: %s y %s' % (dominios_validos[0], dominios_validos[1]))
        else:
            err.append('[Err]: la estructura contemplada de un mail valido es "username_valido@dominio_valido.com"')
        return err
    def verif_espacios_intermedios(self, key, val):
        err=[]
        if (' ' in val) and (key not in ('user_id', 'cuenta_id', 'usuario', 'ciudad', 'pais')):
            err.append(f'[Err]: el campo {key} contiene espacios en blanco')
        return err
    def verif_campo_vacio(self, key, val):
        err=[]
        if (val == '') and (key not in ('user_id', 'cuenta_id', 'usuario')):
            err.append(f'[Err]: el campo {key} esta vacio')
        return err
    # validaciones de usuario
    def validar_datos(self, key, val):
        if key == 'ciudad':
            val[1] = val[1].strip()
            err = self.verif_campo_vacio(key, val[1])
            err = self.verif_espacios_intermedios(key, val[1])
        elif key == 'login_pass':
            # pass 1
            val[0] = val[0].strip()
            err = self.verif_campo_vacio(key, val[0])
            err = self.verif_espacios_intermedios(key, val[0])
            # pass 2
            val[1] = val[1].strip()
            err = self.verif_campo_vacio(key, val[1])
            err = self.verif_espacios_intermedios(key, val[1])
        else:
            val = val.strip()
            err = self.verif_campo_vacio(key, val)
            err = self.verif_espacios_intermedios(key, val)
        if err == []:
            if key == 'nombre':
                val = val.capitalize()
                if (len(val) < 2) or (len(val) > 12):
                    err.append('[Err]: el nombre debe contener entre 2 y 12 caracteres')
            elif key == 'apellido':
                val = val.capitalize()
                if (len(val) < 2) or (len(val) > 12):
                    err.append('[Err]: el apellido debe contener entre 2 y 12 caracteres')
            elif key == 'edad':
                if not(val.isdigit()):
                    err.append('[Err]: la edad debe ser una caracter numerico')
                else:
                    if (int(val) < 1) or (int(val) > 99):
                        err.append('[Err]: la edad esta contemplada como un numero entero positivo menor a 99')
            elif key == 'genero':
                val = val.capitalize()
                if val.lower() not in ('m', 'f'):
                    err.append('[Err]: el genero esta contemplado como -> "m" (masculino) o "f" (femenino)')
            elif key == 'pais':
                val = val.capitalize()
                query = 'select id from paises where nombre = %s'
                values = (val, )
                self.__mydb.ejecutar(query, values)
                r = self.__mydb.get_cursor().fetchall()
                if r == []:
                    err.append('[Err]: no se encontro el pais especificado')
                else:
                    val = r[0][0]
            elif key == 'ciudad':
                if type(val[0]).__name__ != 'list':
                    val[1] = val[1].capitalize()
                    query = 'SELECT ciudades.ciudad_id FROM ciudades INNER JOIN paises ON ciudades.pais_codigo = paises.codigo AND paises.id = %s WHERE ciudades.nombre = %s;'
                    values = (*val, )
                    self.__mydb.ejecutar(query, values)
                    r = self.__mydb.get_cursor().fetchall()
                    if r == []:
                        err.append('[Err]: no se encontro la ciudad ingresada (o no pertenece al pais especificado con anterioridad)')
                    else:
                        val = r[0][0]
                else:
                    err.append('[Err]: es necesario ingresar un pais valido para validar la ciudad')
            elif key == 'telefono':
                if not(val.isdigit()):
                    err.append('[Err]: el numero de telefono debe ser una caracter numerico')
                else:
                    if int(val) < 0:
                        err.append('[Err]: el numero de telefono esta contemplado como un numero entero positivo')
            elif key == 'login_name':
                if (len(val) < 6) or (len(val) > 12):
                    err.append('[Err]: el login_name debe contener entre 6 y 12 caracteres')
                qry = 'select cuenta_id from cuentas where login_name = %s;'
                self.__mydb.ejecutar(qry, (val, ))
                if self.__mydb.get_cursor().fetchall() != []:
                    err.append('[Err]: el nombre de login ingresado ya se encuentra en uso')
            elif key == 'login_pass':
                if val[0] != val[1]:
                    err.append('[Err]: las contraseñas no coinciden')
                if len(val[0]) < 8:
                    err.append('[Err]: el login_pass debe contener minimo 8 caracteres')
                val = val[0]
            elif key == 'l_login_name':
                if (len(val) < 6) or (len(val) > 12):
                    err.append('[Err]: el login_name debe contener entre 6 y 12 caracteres')
            elif key == 'l_login_pass':
                if len(val) < 8:
                    err.append('[Err]: el login_pass debe contener minimo 8 caracteres')
            elif key == 'mail_primario':
                err = self.validar_mail(val)
            elif key == 'mail_secundario':
                err = self.validar_mail(val)
        return err if len(err)>0 else val
    # validadores generales
    # v general de usuario
    def validar_datos_de_usuario(self, dic):
        d_errores = {}
        d_final = {}
        d_temp = {}
        for key, val in dic.items():
            if key == 'ciudad':
                pais_ciudad = [d_temp['pais'], val]
                d_temp[key] = self.validar_datos(key, pais_ciudad)
            else:
                d_temp[key] = self.validar_datos(key, val)
        err_count=0
        for k, v in d_temp.items():
            if type(v).__name__ == 'list':
                err_count+=1
                d_errores[k] = v
            else:
                d_final[k] = v
        if err_count > 0:
            return 1, d_errores
        else:
            return 0, d_final
    # v general de registro
    def validar_registro(self, dic):
        d_errores = {}
        d_final = {}
        d_temp = {}
        err_count = 0
        for key, val in dic.items():
            d_temp[key] = self.validar_datos(key, val)
        for k, v in d_temp.items():
            if type(v).__name__ == 'list':
                err_count+=1
                d_errores[k] = v
            else:
                d_final[k] = v
        if err_count > 0:
            return 1, d_errores
        else:
            return 0, d_final
    # v general de login
    def validar_login(self, dic):
        d_errores = {}
        d_final = {}
        d_temp = {}
        for key, val in dic.items():
            if key == 'login_name':
                d_temp[key] = self.validar_datos('l_login_name', val)
            elif key == 'login_pass':
                d_temp[key] = self.validar_datos('l_login_pass', val)
            else:
                d_temp[key] = self.validar_datos(key, val)
        err_count=0
        for k, v in d_temp.items():
            if type(v).__name__ == 'list':
                err_count+=1
                d_errores[k] = v
            else:
                d_final[k] = v
        if err_count > 0:
            return 1, d_errores
        else:
            return 0, d_final
