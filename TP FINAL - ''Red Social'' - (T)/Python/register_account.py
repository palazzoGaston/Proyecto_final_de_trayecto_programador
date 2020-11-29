# import
from dba import DataBase
from validador import Validador
from cuenta import Cuenta
from usuario import Usuario

# class
class Register():
    # cnstr
    def __init__(self, database=DataBase):
        self.__db = database
        self.__vld = Validador(self.__db)
    # methds
    def register_account(self):
        print('\nPantalla de registro ↓\n\n*Nota: todos los campos son obligatorios!')
        # validando datos de usuario
            # creacion de usuario (en tiempo de ejecucion)
        form_user = {
            'user_id' : 0,
            'nombre' : input('\n<nombre>: '),
            'apellido' : input('\n<apellido>: '),
            'edad' : input('\n<edad>: '),
            'pais' : input('\n<pais>: '),
            'ciudad' : input('\n<ciudad>: '),
            'genero' : input('\n<genero>: '),
            'tel' : input('\n<telefono>: ')
        }
        r, dic=self.__vld.validar_datos_de_usuario(form_user)
        if r == 0:
            nuevo_usuario = Usuario(**dic)
            # validando datos de cuenta
                # creacion de cuenta (en tiempo de ejecucion)
            form_acc = {
                'cuenta_id' : 0,
                'login_name' : input('\n<login_name>: '),
                'login_pass' : [input('\n<login_pass>: '), input('\n<login_pass_confirmacion>: ')],
                'usuario' : 0,
                'mail_primario' : input('\n<mail_primario>: '),
                'mail_secundario' : input('\n<mail_secundario>: ')
            }
            r, dic=self.__vld.validar_registro(form_acc)
            dic['database'] = self.__db
            if r==0:
                nueva_cuenta = Cuenta(**dic)
                # guardar cambios en bd
                opc = input('\nConfirmar creacion de cuenta (s/n): ')
                if opc.lower() == 's':
                    # agregando datos de usuario a la bd ↓
                    ult_id = nuevo_usuario.save_user() # guardando datos de usuario en bd
                    nuevo_usuario.set_user_id(ult_id) # actualizando id de usuario

                    nueva_cuenta.set_usuario(nuevo_usuario) # <- actualizando nuevo usuario en su cuenta

                    # agregando datos de cuenta a la bd ↓
                    ult_id = nueva_cuenta.save_account() # guardando datos de cuenta en bd
                    nueva_cuenta.set_cuenta_id(ult_id) # actualizando id de cuenta

                    print(f'\n[MENSAGE]: el usuario {nueva_cuenta.get_login_name()} ah sido registrado correctamente!')
                else:
                    print('\n[MENSAGE]: Se cancelo el registro de cuenta.')
            else:
                print(f'\n[Err]: uno o mas datos no pudieron validarse ↓')
                for val in dic.values():
                    if type(val).__name__ not in ['DataBase']:
                        for i in val:
                            print(f'\t{i}')
        else:
            print(f'\n[Err]: uno o mas datos no pudieron validarse ↓')
            for val in dic.values():
                for i in val:
                    print(f'\t{i}')