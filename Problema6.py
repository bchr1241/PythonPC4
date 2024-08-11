def contar_lineas_codigo(ruta_archivo):
    if not ruta_archivo.lower().endswith('.py'):
        print("El archivo debe tener una extensión .py")
        return

    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas_codigo = 0
            for linea in archivo:
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    lineas_codigo += 1
            print(f"Número de líneas de código: {lineas_codigo}")

    except FileNotFoundError:
        print("El archivo no se encuentra en la ruta especificada.")
    except Exception:
        print(f"Ocurrió un error")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()
