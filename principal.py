import os
import menus as menu

alumnos ={}
isActive = True
opMenu=0

while (isActive) :
    os.system("cls")
    try:
        opMenu = menu.menuPrincipal()
    except ValueError:
        print("Error en el dato de de ingreso")
        os.system("pause")
    else:
        if(opMenu == 4):
            isActive = False