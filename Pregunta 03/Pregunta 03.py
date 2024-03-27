class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * (self.radio ** 2)


# Ejemplo de uso de la clase Circulo
if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    print("El área del círculo es:", circulo.calcular_area())
