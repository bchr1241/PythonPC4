import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    try:
        fuentes = figlet.getFonts()
    except Exception:
        print("Error al obtener la lista de fuentes")
        return

    fuente_usuario = input("Ingrese el nombre de una fuente (presione Enter para una fuente aleatoria): ")

    if fuente_usuario == "":
        fuente_seleccionada = random.choice(fuentes)
    else:
        if fuente_usuario in fuentes:
            fuente_seleccionada = fuente_usuario
        else:
            print(f"La fuente '{fuente_usuario}' no es válida. Se seleccionará una fuente aleatoria.")
            fuente_seleccionada = random.choice(fuentes)

    texto_imprimir = input("Ingrese el texto a imprimir: ")

    try:
        figlet.setFont(font=fuente_seleccionada)
    except Exception:
        print(f"Error al configurar la fuente '{fuente_seleccionada}'")
        return

    try:
        texto_formateado = figlet.renderText(texto_imprimir)
        print(texto_formateado)
    except Exception:
        print("Error al renderizar el texto")

if __name__ == "__main__":
    main()