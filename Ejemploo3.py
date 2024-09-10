# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Parámetros:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    return base * altura

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    return 0.5 * base * altura

# Función principal
def main():
    """
    Función principal que solicita los valores de base y altura para
    un rectángulo y un triángulo, calcula sus áreas y las imprime.
    """
    try:
        # Cálculo del área del rectángulo
        base_rect = float(input("Ingrese la base del rectángulo: "))
        altura_rect = float(input("Ingrese la altura del rectángulo: "))
        rect_area = calcular_area_rectangulo(base_rect, altura_rect)
        print("Área del rectángulo:", rect_area)

        # Cálculo del área del triángulo
        base_tri = float(input("Ingrese la base del triángulo: "))
        altura_tri = float(input("Ingrese la altura del triángulo: "))
        tri_area = calcular_area_triangulo(base_tri, altura_tri)
        print("Área del triángulo:", tri_area)

    except ValueError:
        print("Por favor, ingrese números válidos.")

if __name__ == "__main__":
    main()
