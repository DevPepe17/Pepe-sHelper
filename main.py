import os
from src.inicio.info import info
from src.inicio.actualiza_sys import actualizar_windows
from src.inicio.actualiza_drivers import menu_drivers
from src.inicio.instalaciones import menu_instalar
from src.mantenimiento.borrar_temporales import borrar_temp
from src.mantenimiento.chksdk import menu_chksdk
from src.mantenimiento.sfc import menu_sfc
from src.mantenimiento.dism import menu_dism


def clear():
    try: os.system("cls")
    except: pass

def panel():
    print("=======SECURITY PEPE'S=======")
    print()
    print("=======INICIO=======")
    print("1. Informacion del sistema")
    print("2. Activar licencia")
    print("3. Actualizar sistema")
    print("4. Actualizar drivers")
    print("5. Instalaciones de sofwares")
    print()
    print("=======MANTENIMIENTO=======")
    print("6. Borrar archivos temporales")
    print("7. Ejecutar CHKSDK en la particion de windows")
    print("8. Ejecutar comprobador de archivos del sistema")
    print("9. Escanear la imagen de Windows")
    print("10. Reparar las configuraciones de winsock")
    print("11. Salir")
    print()

def menu():
    while True:
        clear()
        panel()
        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1": info()
            case "2": pass
            case "3": actualizar_windows()
            case "4": menu_drivers()
            case "5": menu_instalar()
            case "6": borrar_temp()
            case "7": menu_chksdk()
            case "8": menu_sfc()
            case "9": menu_dism()
            case "10": pass
            case "11": break
            case _:
                print("Opción inválida.")
                input("Presiona ENTER para continuar")


