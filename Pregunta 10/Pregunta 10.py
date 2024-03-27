class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * (self.radio ** 2)


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


# Función para mostrar el menú
def mostrar_menu():
    print("Menú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")


# Función principal del menú
def menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print("El área del círculo es:", circulo.calcular_area())
        elif opcion == '2':
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            rectangulo = Rectangulo(base, altura)
            print("El área del rectángulo es:", rectangulo.calcular_area())
        elif opcion == '3':
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print("El área del cuadrado es:", cuadrado.calcular_area())
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


if __name__ == "__main__":
    menu()
