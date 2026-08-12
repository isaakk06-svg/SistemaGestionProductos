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


def buscar_producto():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").lower()

    if not nombre_buscar.strip():
        print("Debe ingresar un nombre para buscar.")
        return

    encontrados = []

    for producto in productos:
        if nombre_buscar in producto["nombre"].lower():
            encontrados.append(producto)

    if not encontrados:
        print("No se encontraron productos.")
        return

    print("\n--- PRODUCTOS ENCONTRADOS ---")

    for i, producto in enumerate(encontrados, start=1):
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
	print("3. Buscar producto")
	print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_productos()

       elif opcion == "3":
    buscar_producto()

	elif opcion == "4":
    print("Programa finalizado.")
    break


menu()