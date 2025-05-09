def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
        print(f"Se agregó {cantidad} unidades a '{producto}'. Total: {inventario[producto]}")
    else:
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")