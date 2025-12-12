import os
import subprocess

def escaneo():
    os.system("cls")
    try:
        proceso = subprocess.Popen('DISM /Online /Cleanup-Image /CheckHealth', shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def escaneo_profundo():
    os.system("cls")
    try:
        proceso = subprocess.Popen('DISM /Online /Cleanup-Image /ScanHealth', shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def reparacion():
    os.system("cls")
    try:
        proceso = subprocess.Popen('DISM /Online /Cleanup-Image /RestoreHealth', shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def limpieza():
    os.system("cls")
    try:
        proceso = subprocess.Popen('DISM /Online /Cleanup-Image /StartComponentCleanup', shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def limpieza_profunda():
    os.system("cls")
    try:
        proceso = subprocess.Popen('DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase', shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def menu_dism():
    while True:
        os.system("cls")
        print("1. Escaneo")
        print("2. Escaneo profundo")
        print("3. Reparacion de la imagen")
        print("4. Limpieza de componentes")
        print("5. Limpieza profunda")
        print("6. Salir")
        opcion = input("\nSelecciona una opción: ")

        match opcion:
            case "1": escaneo()
            case "2": escaneo_profundo()
            case "3": reparacion()
            case "4": limpieza()
            case "5": limpieza_profunda()
            case "6": break
            case _: 
                print("Opción inválida, intenta de nuevo.")
                input("\nPresiona Enter para continuar...")

                
    