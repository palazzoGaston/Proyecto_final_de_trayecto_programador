# imports
from dba import DataBase
from register_account import Register
from session_controller import SessionController
# main
print('\n|RedSocial|')
db = DataBase() # data base
reg = Register(db) # create account
sse_ctrl = SessionController(db) # gestor de sesion
    # pantalla principal
while True:
    print(f'\n\tOPCIONES:\n1. Logear\n2. Registrarse\n0. Exit')
    opc=input('\n<opcion>: ')
    if opc=='0':
        break
    elif opc=='1':
        usuario_activo = sse_ctrl.inciar_sesion()
        if (type(usuario_activo).__name__).lower() == 'cuenta':
            sse_ctrl.menu_principal(usuario_activo)
    elif opc=='2':
        reg.register_account()
    else:
        print('\n[Err]: Opcion incorrecta!')

print('\n[MENSAJE]: Fin de la ejecucion!\n')