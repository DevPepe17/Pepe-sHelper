# 🛡️ Pepe's Helper: Solución Integral de Mantenimiento y Diagnóstico para PC

## 📝 Descripción del Proyecto

**Pepe's Helper** es un software diseñado para facilitar las tareas esenciales de mantenimiento, diagnóstico y reparación de computadoras con sistema operativo Windows. Este proyecto centraliza múltiples comandos y scripts de reparación y optimización, permitiendo a los usuarios mantener su PC funcionando de manera óptima y solucionar problemas comunes con una interfaz sencilla.

## 🚀 Funcionalidades Principales

El software se divide en dos grandes áreas: **Diagnóstico Inicial** y **Mantenimiento/Reparación Avanzada**.

### 1. ⚙️ Diagnóstico y Obtención de Información (src/inicio)

Módulos dedicados a la recopilación de datos vitales del sistema y la configuración inicial:

* **Información de Componentes (`info.py`):** Muestra detalles exhaustivos del hardware (CPU, RAM, Tarjeta Gráfica, Discos Duros) y del sistema operativo instalado.
* **Actualización de Controladores (`actualiza_drivers.py`):** Ejecuta rutinas para verificar y actualizar controladores de dispositivos.
* **Actualización del Sistema (`actualiza_sys.py`):** Verifica e instala las últimas actualizaciones críticas y de seguridad de Windows.
* **Instalaciones (`instalaciones.py`):** Gestión de utilidades y software común.

### 2. 🔨 Reparación y Mantenimiento (src/mantenimiento)

Módulos enfocados en la reparación y optimización del sistema:

* **Borrado de Archivos Temporales (`borrar_temporales.py`):** Limpia archivos basura, caché y temporales para liberar espacio y mejorar el rendimiento.
* **Comprobación de Disco (`chksdk.py`):** Ejecuta comandos de verificación y reparación del sistema de archivos en los discos duros (similar a `chkdsk`).
* **Mantenimiento de Imagen del Sistema (`dism.py`):** Utiliza la herramienta DISM (Deployment Image Servicing and Management) para reparar y preparar imágenes de Windows.
* **Comprobador de Archivos del Sistema (`sfc.py`):** Ejecuta el comando SFC (System File Checker) para escanear y reparar archivos de sistema dañados o corruptos.

## 💻 Requisitos del Sistema

* Sistema Operativo: Windows 10/11 (Se recomienda ejecutar con permisos de administrador).
