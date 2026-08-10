productos = []


def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(producto)

    print("Producto agregado correctamente.")


def mostrar_productos():
    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- LISTA DE PRODUCTOS ---")

    for i, producto in enumerate(productos, start=1):
        print(
            f"{i}. {producto['nombre']} | "
            f"Precio: ${producto['precio']:.2f} | "
            f"Cantidad: {producto['cantidad']}"
        )


def menu():
    while True:
        print("\n=================================")
        print("   SISTEMA DE GESTIÓN DE PRODUCTOS")
        print("=================================")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


menu()