def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
        print(f"Producto '{producto}' eliminado del inventario.")
    else:
        print(f"Error: Producto '{producto}' no encontrado.")