# import
from usuario import Usuario
from cuenta import Cuenta
from login_account import Login
from dba import DataBase
from validador import Validador
from menu_principal import MenuPrincipal

# class
class SessionController():

    # cnstr
    def __init__(self, database=DataBase):
        self.__bd = database
        self.__log = Login(self.__bd)
        self.__vld = Validador(self.__bd)
    
    # mthds
    def inciar_sesion(self):
        log = self.__log.login_account()
        if (type(log).__name__).lower() == 'cuenta':
            MenuPrincipal(log, self.__vld).MostrarOpciones()