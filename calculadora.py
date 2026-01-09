def es_primo(numero):
    """Función que verifica si un número es primo y devuelve sus divisores si no lo es."""
    if numero < 2:
        return False, []
    divisores = []
    for i in range(2, numero):
        if numero % i == 0:
            divisores.append(i)
    if len(divisores) == 0:
        return True, []
    else:
        return False, divisores
def main():
    while True:
        entrada = input("Ingrese un número entero positivo (o 'salir' para terminar): ")
        if entrada.lower() == "salir":
            print("Programa terminado.")
            break
        if not entrada.isdigit():  # Verifica si es un número positivo
            print("Error: Debe ingresar un número entero positivo.")
            continue
        numero = int(entrada)
        if numero <= 0:
            print("Error: El número debe ser mayor que 0.")
            continue
        primo, divisores = es_primo(numero)
        if primo:
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo. Sus divisores son: {divisores}")
# Ejecutar el programa
main()