class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No especificada")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No especificadas")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.notas.append(nota)


# Ejemplo de uso de la clase Alumno
if __name__ == "__main__":
    # Creamos un objeto Alumno
    alumno1 = Alumno("Luis", "2212648")
    
    # Mostramos la información inicial del alumno
    alumno1.display()
    
    # Asignamos la edad y algunas notas al alumno
    alumno1.setAge(18)
    alumno1.setNota(20)
    alumno1.setNota(20)
    
    # Mostramos la información actualizada del alumno
    alumno1.display()

