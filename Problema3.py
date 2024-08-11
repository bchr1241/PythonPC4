import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagen descargada y guardada como {nombre_archivo}")
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

def comprimir_archivo(nombre_archivo):
    zip_name = nombre_archivo.split('.')[0] + '.zip'
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            zipf.write(nombre_archivo, os.path.basename(nombre_archivo))
        print(f"Archivo comprimido creado como {zip_name}")
    except Exception as e:
        print(f"Error al crear el archivo ZIP: {e}")

def descomprimir_archivo(zip_name):
    try:
        with zipfile.ZipFile(zip_name, 'r') as zipf:
            zipf.extractall()
        print(f"Archivo ZIP {zip_name} descomprimido")
    except Exception as e:
        print(f"Error al descomprimir el archivo ZIP: {e}")

def main():
    url_imagen = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    nombre_archivo_imagen = 'imagen_descargada.jpg'
    
    descargar_imagen(url_imagen, nombre_archivo_imagen)
    
    comprimir_archivo(nombre_archivo_imagen)
    
    zip_name = nombre_archivo_imagen.split('.')[0] + '.zip'
    descomprimir_archivo(zip_name)

if __name__ == "__main__":
    main()

