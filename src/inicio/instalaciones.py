import os
import webbrowser

programas = {
    "1": ("Google Chrome", "https://dl.google.com/dl/chrome/install/googlechromestandaloneenterprise64.msi"),
    "2": ("Mozilla Firefox", "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=es-ES"),
    "3": ("WinRAR", "https://d.winrar.es/d/103z1765315942/m2EvA2vJ-eSI0W3N9jSOMQ/winrar-x64-713es.exe"),
    "4": ("VLC Media Player", "https://mirror.cedia.org.ec/videolan/vlc/3.0.21/win64/vlc-3.0.21-win64.exe")
}

def descargar_programa(opcion):
    if opcion in programas:
        _, url = programas[opcion]
        webbrowser.open(url)
    else: print("Opcion invalida")


def menu_instalar():
    while True:
        os.system("cls")
        print("1. Chorme")
        print("2. Firefox")
        print("3. Winrar")
        print("4. VLC")
        print("5. Salir")

        opcion = input("\nSelecciona una opción: ")
        if opcion == "5": break
        descargar_programa(opcion)
        
