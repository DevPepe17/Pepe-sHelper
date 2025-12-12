import subprocess  
import time
import os

def actualizar_windows():
    os.system("cls")
    print(">>> Buscando actualizaciones...")
    subprocess.run("usoclient StartScan", shell=True)
    time.sleep(3)

    print(">>> Descargando actualizaciones...")
    subprocess.run("usoclient StartDownload", shell=True)
    time.sleep(3)

    print(">>> Instalando actualizaciones...")
    subprocess.run("usoclient StartInstall", shell=True)
    time.sleep(3)

    print(">>> Windows ya está completamente actualizado.")
    input("\nPresiona ENTER para volver al menu")
