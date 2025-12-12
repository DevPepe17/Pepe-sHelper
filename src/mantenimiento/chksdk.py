import os
import subprocess

def escanear():
    os.system("cls")
    disco = input("Introduzca la letra de la unidad a escanear (ej: C:): ").upper()
    if not disco.endswith(':') : disco += ':'

    comando = f'chkdsk {disco}'
    try: 
        proceso = subprocess.Popen(comando, shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def corregir_errores():
    os.system("cls")
    disco = input("Introduzca la letra de la unidad a corregir (ej: C:): ").upper()
    if not disco.endswith(':') : disco += ':'

    comando = f'chkdsk {disco} /f'
    try: 
        proceso = subprocess.Popen(comando, shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def reparacion_profunda():
    os.system("cls")
    disco = input("Introduzca la letra de la unidad a reparar (ej: C:): ").upper()
    if not disco.endswith(':') : disco += ':'

    comando = f'chkdsk {disco} /r'
    try: 
        proceso = subprocess.Popen(comando, shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def escaneo_online():
    os.system("cls")
    disco = input("Introduzca la letra de la unidad a escanear online (ej: C:): ").upper()
    if not disco.endswith(':') : disco += ':'

    comando = f'chkdsk {disco} /scan'
    try: 
        proceso = subprocess.Popen(comando, shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def reparacion_definitiva():
    os.system("cls")
    disco = input("Introduzca la letra de la unidad a escanear online (ej: C:): ").upper()
    if not disco.endswith(':') : disco += ':'

    comando = f'chkdsk {disco} /r /x'
    try: 
        proceso = subprocess.Popen(comando, shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def menu_chksdk():
    while True:
        os.system("cls")
        print("1. Solo Escanear")
        print("2. Corregir errores lógicos")
        print("3. Reparación profunda")
        print("4. Escaneo online")
        print("5. Reparación definitiva")
        print("6. Salir")

        opcion = input("\nSelecciona una opción: ")

        match opcion:
            case "1": escanear()
            case "2": corregir_errores()
            case "3": reparacion_profunda()
            case "4": escaneo_online()
            case "5": reparacion_definitiva()
            case "6": break
            case _:
                print("Opción inválida, intenta de nuevo.")
                input("\nPresiona Enter para continuar...")