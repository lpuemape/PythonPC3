import generador_numeros

def main():
    lista_numeros = generador_numeros.generar_numeros()
    generador_numeros.mostrar_lista(lista_numeros)
    generador_numeros.ordenar_lista(lista_numeros)

if __name__ == "__main__":
    main()
