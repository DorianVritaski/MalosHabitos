def calcular(a, b, c):
    """
    Calcula el resultado de la expresión: a * b + c

    Parámetros:
    a (int o float): Primer número a multiplicar.
    b (int o float): Segundo número a multiplicar.
    c (int o float): Número que se suma al resultado de a * b.

    Retorna:
    int o float: Resultado de la operación.
    """
    return a * b + c


def principal():
    """
    Función principal que solicita al usuario ingresar los valores de x, y, z
    y calcula el resultado de la operación a través de la función calcular().
    """
    try:
        x = float(input("Ingrese el valor de x: "))
        y = float(input("Ingrese el valor de y: "))
        z = float(input("Ingrese el valor de z: "))

        resultado = calcular(x, y, z)
        print("El resultado es:", resultado)
    except ValueError:
        print("Por favor, ingrese números válidos.")


if __name__ == "__main__":
    principal()

