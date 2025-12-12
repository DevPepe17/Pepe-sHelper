import subprocess
import json
import os
import webbrowser

def obtener_dispositivos():
    comando = ["powershell",
        "-Command",
        "Get-CimInstance Win32_PnPEntity | "
        "Select-Object Status, Name | "
        "ConvertTo-Json -Compress"]

    try: 
        resultado = subprocess.run(comando, capture_output=True, text=True)
        dispositivos = json.loads(resultado.stdout)
    except:
        print("Error al obtener los dispositivos")
        return [], []
    
    errores = [ d.get('Name', 'Sin nombre') 
               for d in dispositivos
               if d.get('Status', 'Desconocido').lower() != 'ok']

    return dispositivos, errores

def actualizar_dispositivos_auto():
    _, errores = obtener_dispositivos()

    fabricantes_prohibidos = [
        "NVIDIA", "AMD", "Advanced Micro Devices", "Intel",
        "Realtek", "MediaTek", "Broadcom", "Qualcomm",
        "Synaptics", "ELAN", "ASUS", "MSI", "Lenovo"
    ]

    try:
        if not errores: print("No hay dispositivos para actualizar")
        else:
            for idx, nombre in enumerate(errores, 1):
                print(f"{idx}. {nombre}")
            confirmar = input("\n¿Deseas actualizar estos dispositivos? (s/n): ").strip().lower()
            if confirmar != "s": return print("Actualización cancelada.")

            for nombre in errores:
                if any(fab.lower() in nombre.lower() for fab in fabricantes_prohibidos):
                    print(f"Omitido: {nombre} (driver delicado, instalar manualmente)")
                    continue

                comando = ["powershell", "-Command",
                f"Get-PnpDevice | Where-Object {{$_.FriendlyName -eq '{nombre}' -or $_.Name -eq '{nombre}'}} | "
                f"ForEach-Object {{ Update-PnpDevice -InstanceId $_.InstanceId -Confirm:$false }}"]
                resultado = subprocess.run(comando, capture_output=True, text=True)
                print(f"Actualizado: {nombre}")
            print("Actualización de dispositivos completada")
    except:
        print("Ocurrió un error")


def actualizar_dispositivos_manual():
    _, errores = obtener_dispositivos()

    fabricantes_prohibidos = {
        "amd": "https://www.amd.com/es/support/download/drivers.html",
        "advanced micro devices": "https://www.amd.com/es/support/download/drivers.html",
        "nvidia": "https://www.nvidia.com/en-us/drivers/",
        "intel": "https://www.intel.com/content/www/us/en/support/detect.html",
        "realtek": "https://www.realtek.com/Download/Index?cate_id=194&menu_id=297",
        "mediatek": None,
        "broadcom": None,
        "qualcomm": None,
        "synaptics": None,
        "elan": None,
        "asus": None,
        "msi": None,
        "lenovo": None
    }

    try:
        if not errores: return print("No hay dispositivos para actualizar")
        else:
            dispositivos_criticos = []
            for nombre in errores:
                nombre_lower = nombre.lower()
                for fab, url in fabricantes_prohibidos.items():
                    if fab in nombre_lower:
                        dispositivos_criticos.append((nombre, url))
                        break

            if not dispositivos_criticos: return print("No se detectaron dispositivos críticos")
            else:
                for idx, (nombre, _) in enumerate(dispositivos_criticos, 1):
                    print(f"{idx}. {nombre}")
                
                confirmar = input("\n¿Deseas abrir las páginas de descarga? (s/n): ").strip().lower()
                if confirmar != "s": return print("Operación cancelada.")
                for _, url in dispositivos_criticos:
                    webbrowser.open(url)
    except:
        print("Ocurrió un error")

def menu_drivers():
    while True:
        os.system("cls")
        print("====== DRIVERS ======")
        print("1. Ver dispositivos conectados")
        print("2. Actualizar drivers (automático)")
        print("3. Actualizar drivers (manual)")
        print("4. Salir")
        opcion = input("\nSelecciona una opción: ")

        match opcion:
            case "1":
                os.system("cls")
                dispositivos, _ = obtener_dispositivos()
                for d in dispositivos:
                    status = d.get('Status', 'Desconocido')
                    nombre = d.get('Name', 'Sin nombre')
                    print(f"[{status}] {nombre}")
                input("\nPresiona Enter para regresar al menú...")
            case "2":
                os.system("cls")
                actualizar_dispositivos_auto()
                input("\nPresiona Enter para regresar al menú...")
            case "3":
                os.system("cls")
                actualizar_dispositivos_manual()
                input("\nPresiona Enter para regresar al menú...")
            case "4":
                break
            case _:
                print("Opción inválida, intenta de nuevo.")
                input("\nPresiona Enter para continuar...")
            
