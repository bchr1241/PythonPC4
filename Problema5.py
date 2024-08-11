import os

def solicitar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if 1 <= numero <= 10:
                return numero
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def guardar_tabla_multiplicar(numero):
    nombre_archivo = f"tabla-{numero}.txt"
    try:
        with open(nombre_archivo, 'w') as archivo:
            for i in range(1, 11):
                archivo.write(f"{numero} x {i} = {numero * i}\n")
        print(f"Tabla de multiplicar del {numero} guardada en {nombre_archivo}.")
    except Exception:
        print("Error al guardar la tabla de multiplicar")

def leer_tabla_multiplicar(numero):
    nombre_archivo = f"tabla-{numero}.txt"
    if os.path.isfile(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                print(archivo.read())
        except Exception:
            print("Error al leer el archivo")
    else:
        print(f"El archivo {nombre_archivo} no existe.")

def mostrar_linea_tabla(numero, m):
    nombre_archivo = f"tabla-{numero}.txt"
    if os.path.isfile(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                if 1 <= m <= len(lineas):
                    print(lineas[m-1].strip())
                else:
                    print("Número de línea fuera del rango.")
        except Exception:
            print("Error al leer el archivo")
    else:
        print(f"El archivo {nombre_archivo} no existe.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar la tabla de multiplicar en un archivo")
        print("2. Leer y mostrar la tabla de multiplicar desde el archivo")
        print("3. Mostrar una línea específica de la tabla de multiplicar")
        print("4. Salir")
        
        opcion = solicitar_numero("Seleccione una opción (1-4): ")
        
        if opcion == 1:
            numero = solicitar_numero("Ingrese un número entero entre 1 y 10: ")
            guardar_tabla_multiplicar(numero)
        elif opcion == 2:
            numero = solicitar_numero("Ingrese el número de la tabla que desea leer (entre 1 y 10): ")
            leer_tabla_multiplicar(numero)
        elif opcion == 3:
            numero = solicitar_numero("Ingrese el número de la tabla (entre 1 y 10): ")
            m = solicitar_numero("Ingrese el número de la línea que desea ver (entre 1 y 10): ")
            mostrar_linea_tabla(numero, m)
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

if __name__ == "__main__":
    menu()
