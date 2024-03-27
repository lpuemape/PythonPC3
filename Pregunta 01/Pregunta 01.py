def obtener_porcentaje(fraction):
    try:
        numerador, denominador = map(int, fraction.split('/'))
        if denominador == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        elif numerador <= 0 or denominador <= 0:
            raise ValueError("Los números deben ser enteros positivos.")
        elif numerador > denominador:
            raise ValueError("El numerador debe ser menor o igual al denominador.")
        
        porcentaje = (numerador / denominador) * 100

        if porcentaje < 1:
            return 'E'
        elif porcentaje > 99:
            return 'F'
        else:
            return str(round(porcentaje)) + '%'
    except ValueError as e:
        print("Error:", e)
        return None
    except ZeroDivisionError as e:
        print("Error:", e)
        return None

def main():
    while True:
        fraction = input("Ingrese una fracción en formato X/Y (donde X e Y son enteros): ")
        resultado = obtener_porcentaje(fraction)
        if resultado:
            print("Cantidad de combustible en el tanque:", resultado)
            break

if __name__ == '__main__':
    main()
S