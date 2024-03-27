def obtener_calificaciones():
    while True:
        try:
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones_lista = calificaciones_str.split(',')
            calificaciones_enteros = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Por favor, asegúrese de ingresar solo números separados por comas.")

if __name__ == "__main__":
    calificaciones = obtener_calificaciones()
    print("Calificaciones ingresadas:", calificaciones)
