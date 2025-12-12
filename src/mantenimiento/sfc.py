import os
import subprocess

def escanear():
    os.system("cls")
    try:
        proceso = subprocess.Popen('sfc /verifyonly', shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def reparar():
    os.system("cls")
    try:
        proceso = subprocess.Popen('sfc /scannow', shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
    except: print("ERROR inesperado durante la ejecución")

def menu_sfc():
    while True:
        os.system("cls")
        print("1. Solo escanear")
        print("2. Escanear y reparar")
        print("3. Salir")
        opcion = input("\nSelecciona una opción: ")

        match opcion:
            case "1": escanear()
            case "2": reparar()
            case "3": break
            case _: 
                print("Opción inválida, intenta de nuevo.")
                input("\nPresiona Enter para continuar...")

                