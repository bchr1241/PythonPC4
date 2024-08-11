import csv
import requests

def descargar_archivo(url, nombre_archivo):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si la solicitud fue exitosa
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)
        print(f"Archivo descargado y guardado como '{nombre_archivo}'.")
    except requests.RequestException:
        print(f"Error al descargar el archivo")

def leer_temperaturas(ruta_archivo):
    temperaturas = []
    try:
        with open(ruta_archivo, 'r') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 2:
                    try:
                        temperatura = float(fila[1])
                        temperaturas.append(temperatura)
                    except ValueError:
                        print(f"Advertencia: La temperatura '{fila[1]}' no es un número válido y será ignorada.")
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encuentra.")
    except Exception:
        print(f"Error inesperado")
    return temperaturas

def calcular_estadisticas(temperaturas):
    if not temperaturas:
        return None, None, None
    
    promedio = sum(temperaturas) / len(temperaturas)
    max_temp = max(temperaturas)
    min_temp = min(temperaturas)
    return promedio, max_temp, min_temp

def escribir_resumen(ruta_archivo, promedio, max_temp, min_temp):
    try:
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(f"Temperatura Promedio: {promedio:.2f}\n")
            archivo.write(f"Temperatura Máxima: {max_temp:.2f}\n")
            archivo.write(f"Temperatura Mínima: {min_temp:.2f}\n")
    except Exception:
        print(f"Error al escribir el archivo")

def main():
    url = 'https://github.com/gdelgador/ProgramacionPython202407/blob/main/Modulo4/src/temperaturas.txt?raw=true'
    archivo_descargado = 'temperaturas.txt'
    archivo_salida = 'resumen_temperaturas.txt'
    
    descargar_archivo(url, archivo_descargado)
    
    temperaturas = leer_temperaturas(archivo_descargado)
    
    promedio, max_temp, min_temp = calcular_estadisticas(temperaturas)
    
    if promedio is not None:
        escribir_resumen(archivo_salida, promedio, max_temp, min_temp)
        print(f"Resumen de temperaturas guardado en '{archivo_salida}'.")
    else:
        print("No se pudieron calcular las estadísticas debido a que no hay datos válidos.")

if __name__ == "__main__":
    main()
