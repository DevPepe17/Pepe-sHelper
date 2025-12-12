import os
import shutil

def borrar_temp():
    os.system("cls")
    temp_dir = os.environ.get('TEMP') or os.environ.get('TMP')
    
    if not temp_dir or not os.path.exists(temp_dir): return print("ERROR: No se pudo encontrar el directorio temporal. Saliendo.")
    print(f"--- Iniciando limpieza en: {temp_dir} ---\n")
    
    files_deleted = 0
    dirs_deleted = 0
    errors_count = 0

    for item_name in os.listdir(temp_dir):
        item_path = os.path.join(temp_dir, item_name)
        
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Carpeta eliminada: {item_path}")
                dirs_deleted += 1
            elif os.path.isfile(item_path):
                os.remove(item_path)
                print(f"Archivo eliminado: {item_path}")
                files_deleted += 1
        except PermissionError:
            print(f"ERROR de Permiso (en uso): No se pudo eliminar {item_name}")
            errors_count += 1
        except Exception as e:
            print(f"ERROR inesperado al borrar {item_name}: {e}")
            errors_count += 1

    print("\n--- Limpieza Terminada ---")
    print(f"Archivos eliminados: {files_deleted}")
    print(f"Carpetas eliminadas: {dirs_deleted}")
    print(f"Archivos/Carpetas omitidas (en uso): {errors_count}")
    input("\nPresiona ENTER para continuar")
