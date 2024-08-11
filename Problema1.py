import requests

def obtener_precio_bitcoin():
    try:
        url="https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.RequestException:
        print("Error al obtener el precio de Bitcoin")
        return None
    
def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Por favor ingrese un número válido")
        return
    
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        costo_total = n * precio_bitcoin
        print(f"El costo total actual de {n} bitcoins es de ${costo_total:,.4f}")
    else:
        print(f"No se puede obtener el costo total actual de {n} bitcoins")

if __name__ == "__main__":
    main()


