import subprocess
import json
import re
import platform
from datetime import datetime
import os

def fecha(fecha_ms):
    try:
        ms = int(re.search(r'\d+', fecha_ms).group())
        return datetime.fromtimestamp(ms / 1000).strftime("%Y-%m-%d %H:%M:%S")
    except:
        return fecha_ms

def info_sistema():
    comando = ('powershell -NoProfile -Command '
        '"Get-CimInstance Win32_OperatingSystem '
        '| Select-Object Caption, Version, BuildNumber, InstallDate, LastBootUpTime, '
        'SerialNumber, OSArchitecture, WindowsDirectory, Locale, CurrentTimeZone '
        '| ConvertTo-Json"')
    
    proceso = subprocess.run(comando, capture_output=True, text=True, shell=True)

    try: datos = json.loads(proceso.stdout)
    except: 
        print ("No se pudo leer la información del sistema")
        return

    print("==========INFORMACION DEL SISTEMA===============")
    print(f"Nombre del sistema operativo:   {datos.get('Caption', 'N/D')}")
    print(f"Versión:                        {datos.get('Version', 'N/D')} (Build {datos.get('BuildNumber', 'N/D')})")
    print(f"Arquitectura:                   {datos.get('OSArchitecture', 'N/D')}")
    print(f"Fecha de instalación:           {fecha(datos.get('InstallDate', 'N/D'))}")
    print(f"Último arranque:                {fecha(datos.get('LastBootUpTime', 'N/D'))}")
    print(f"Serial / Product ID:            {datos.get('SerialNumber', 'N/D')}")
    print(f"Carpeta de Windows:             {datos.get('WindowsDirectory', 'N/D')}")
    print(f"Idioma del sistema:             {datos.get('Locale', 'N/D')}")
    print()

def info_cpu():
    comando = ('powershell -NoProfile -Command '
        '"Get-CimInstance Win32_Processor | '
        'Select-Object Name, Manufacturer, MaxClockSpeed, NumberOfCores, '
        'NumberOfLogicalProcessors, L2CacheSize, L3CacheSize, VirtualizationFirmwareEnabled | '
        'ConvertTo-Json"')
    
    proceso = subprocess.run(comando, capture_output=True, text=True, shell=True)

    try: datos = json.loads(proceso.stdout)
    except: 
        print ("No se pudo leer la información del CPU")
        return
    
    print("========== INFORMACION DE LA CPU ===========")
    print(f"Modelo:                  {datos.get('Name', 'N/D')}")
    print(f"Fabricante:              {datos.get('Manufacturer', 'N/D')}")
    print(f"Arquitectura:            {platform.machine()}")
    print(f"Velocidad base:          {datos.get('MaxClockSpeed', 'N/D')} MHz")
    print(f"Núcleos físicos:         {datos.get('NumberOfCores', 'N/D')}")
    print(f"Núcleos lógicos:         {datos.get('NumberOfLogicalProcessors', 'N/D')}")
    print(f"Caché L2/L3:             L2:{datos.get('L2CacheSize', 'N/D')} KB / L3:{datos.get('L3CacheSize', 'N/D')} KB")
    print(f"Virtualización:          {datos.get('VirtualizationFirmwareEnabled', 'N/D')}")
    print()

def info_gpu():
    comando = (
        'powershell -NoProfile -Command '
        '"Get-CimInstance Win32_VideoController '
        '| Select-Object Name, AdapterRAM, DriverVersion '
        '| ConvertTo-Json"'
    )

    proceso = subprocess.run(comando, capture_output=True, text=True, shell=True)

    try:
        datos = json.loads(proceso.stdout)
        if isinstance(datos, dict):
            datos = [datos]
    except:
        print("No se pudo leer la información de la GPU.")
        return

    print("========== INFORMACIÓN DE LA GPU ===========")
    for idx, gpu in enumerate(datos, 1):
        nombre = gpu.get('Name', 'N/D')
        vram = int(gpu.get('AdapterRAM', 0)) // (1024**2) 
        driver = gpu.get('DriverVersion', 'N/D')

        if idx != 1:
            print()
        print(f"GPU #{idx}")
        print(f"Modelo:        {nombre}")
        print(f"VRAM total:    {vram} MB")
        print(f"Driver versión: {driver}")
    print()

def info_placa():
    comando = (
        'powershell -NoProfile -Command '
        '"$board = Get-CimInstance Win32_BaseBoard; '
        '$bios = Get-CimInstance Win32_BIOS; '
        '$system = Get-CimInstance Win32_ComputerSystem; '
        '$ramArray = Get-CimInstance Win32_PhysicalMemoryArray; '
        '$totalRAMSlots = $ramArray[0].MemoryDevices; '
        '$usedRAMSlots = (Get-CimInstance Win32_PhysicalMemory).Count; '
        '$bootMode = if ($system.BootupState -match \'EFI\') {\'UEFI\'} else {\'Legacy\'}; '
        '$info = @{Manufacturer=$board.Manufacturer; Product=$board.Product; BIOSVersion=$bios.SMBIOSBIOSVersion; BootMode=$bootMode; TotalRAMSlots=$totalRAMSlots; UsedRAMSlots=$usedRAMSlots}; '
        '$info | ConvertTo-Json -Compress"'
    )

    proceso = subprocess.run(comando, capture_output=True, text=True, shell=True)

    try:
        datos = json.loads(proceso.stdout)
    except Exception as e:
        print("No se pudo leer la información de la placa base:", e)
        return

    total = datos.get('TotalRAMSlots', 0)
    usados = datos.get('UsedRAMSlots', 0)

    print("========== INFORMACIÓN DE LA PLACA BASE ===========")
    print(f"Fabricante:             {datos.get('Manufacturer','N/D')}")
    print(f"Modelo:                 {datos.get('Product','N/D')}")
    print(f"Versión del BIOS:       {datos.get('BIOSVersion','N/D')}")
    print(f"Modo del BIOS:          {datos.get('BootMode','N/D')}")
    print(f"Slots totales:          {total}")
    print(f"Slots ocupados:         {usados}")
    print(f"Slots libres:           {total - usados}")
    print()

def info_ram():
    comando = (
        'powershell -NoProfile -Command '
        '"$mem = Get-CimInstance Win32_PhysicalMemory; '
        '$comp = Get-CimInstance Win32_ComputerSystem; '
        '$total = ($comp.TotalPhysicalMemory / 1MB); '
        '$used = ($total - (Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1024); '
        '@{TotalMB=[math]::Round($total); UsedMB=[math]::Round($used); FreeMB=[math]::Round($total-$used); '
        'Modules=$mem.Count} | ConvertTo-Json -Compress"'
    )

    proceso = subprocess.run(comando, capture_output=True, text=True, shell=True)

    try:
        datos = json.loads(proceso.stdout)
    except Exception as e:
        print("No se pudo leer la información de la RAM:", e)
        return

    print("========== INFORMACIÓN DE RAM ==========")
    print(f"Memoria total instalada: {datos.get('TotalMB','N/D')} MB")
    print(f"Memoria en uso:          {datos.get('UsedMB','N/D')} MB")
    print(f"Memoria disponible:      {datos.get('FreeMB','N/D')} MB")
    print(f"Cantidad de módulos:     {datos.get('Modules','N/D')}")
    print()

def info_almacenamiento():
    comando = (
        'powershell -NoProfile -Command '
        '"$discos = Get-CimInstance Win32_DiskDrive; '
        '$info = @(); '
        'foreach ($d in $discos) { '
        '  $tipo = if ($d.MediaType -match \\"SSD\\") {\\"SSD\\"} else {\\"HDD\\"}; '
        '  $info += @{Name=$d.Caption; Tipo=$tipo; CapacidadGB=[math]::Round($d.Size/1GB); Modelo=$d.Model; Interfaz=$d.InterfaceType}; '
        '} '
        '$info | ConvertTo-Json -Compress"'
    )

    proceso = subprocess.run(comando, capture_output=True, text=True, shell=True)

    try:
        datos = json.loads(proceso.stdout)
        if isinstance(datos, dict):
            datos = [datos]
    except Exception as e:
        print("No se pudo leer la información del almacenamiento:", e)
        return

    print("========== INFORMACIÓN DE ALMACENAMIENTO ==========")
    for idx, disco in enumerate(datos, 1):
        if idx != 1:
            print()
        print(f"Disco #{idx}")
        print(f"Nombre:    {disco.get('Name','N/D')}")
        print(f"Tipo:      {disco.get('Tipo','N/D')}")
        print(f"Capacidad: {disco.get('CapacidadGB','N/D')} GB")
        print(f"Modelo:    {disco.get('Modelo','N/D')}")
        print(f"Interfaz:  {disco.get('Interfaz','N/D')}")
    print()

def info():
    os.system("cls")
    info_sistema()
    info_cpu()
    info_gpu()
    info_placa()
    info_ram()
    info_almacenamiento()
    input("Presiona ENTER para volver al menu")



    