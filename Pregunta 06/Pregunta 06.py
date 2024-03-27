class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio} - Año: {self.año}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)


if __name__ == "__main__":
    # Creamos un catálogo
    catalogo = Catalogo()
    
    # Agregamos algunos productos al catálogo
    catalogo.agregar_producto(Producto("Filtro de aceite", 25.99, 2023))
    catalogo.agregar_producto(Producto("Pastillas de freno", 35.50, 2022))
    catalogo.agregar_producto(Producto("Bujías", 12.75, 2023))
    catalogo.agregar_producto(Producto("Amortiguadores", 89.99, 2022))
    
    # Mostramos la lista de productos
    catalogo.mostrar_productos()
    
    # Filtramos los productos por año
    catalogo.filtrar_por_año(2022)
