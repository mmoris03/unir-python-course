class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int) -> None:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del producto no debe estar en blanco")

        self.nombre = nombre
        self.actualizar_precio(precio)
        self.actualizar_cantidad(cantidad)

    def actualizar_precio(self, nuevo_precio: float) -> None:
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El precio debe ser un número")
        if not nuevo_precio >= 0:
            raise ValueError("El precio debe ser mayor o igual que cero")
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int) -> None:
        if not isinstance(nueva_cantidad, int):
            raise TypeError("La cantidad debe ser un número entero")
        if not nueva_cantidad >= 0:
            raise ValueError("La cantidad debe ser mayor o igual que cero")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad

    def __str__(self) -> str:
        return f"{self.nombre} [Precio: {self.precio:.2f} | Cantidad: {self.cantidad}]"


class Inventario:
    def __init__(self) -> None:
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto")
        self.productos.append(producto)

    def buscar_producto(self, nombre: str) -> Producto | None:
        buscado = nombre.casefold()
        return next((p for p in self.productos if p.nombre.casefold() == buscado), None)

    def calcular_valor_inventario(self) -> float:
        return sum(p.calcular_valor_total() for p in self.productos)

    def listar_productos(self) -> None:
        print("     Productos")
        if self.productos:
            print(*self.productos, sep="\n")
        else:
            print("No hay productos en el inventario")


def _pedir_nombre() -> str:
    return input("Nombre: ")


def _pedir_precio() -> float:
    while True:
        try:
            return float(input("Precio: ").replace(",", "."))
        except ValueError:
            print("El precio debe ser un número")


def _pedir_cantidad() -> int:
    while True:
        try:
            return int(input("Cantidad: "))
        except ValueError:
            print("La cantidad debe ser un número entero")


def _pedir_producto() -> Producto:
    return Producto(
        _pedir_nombre(),
        _pedir_precio(),
        _pedir_cantidad()
    )


def _agregar_producto_pedido(inventario: Inventario) -> None:
    try:
        inventario.agregar_producto(_pedir_producto())
    except (ValueError, TypeError) as error:
        print(f"No se pudo agregar el producto: {error}")


def _mostrar_producto_buscado(inventario: Inventario) -> None:
    nombre = _pedir_nombre()
    producto = inventario.buscar_producto(nombre)
    print(
        producto
        if producto
        else f"No hay ningún producto con nombre \"{nombre}\" en el inventario"
    )


def _mostrar_total_inventario(inventario: Inventario) -> None:
    print(f"Total inventario: {inventario.calcular_valor_inventario():.2f}")


OPCIONES = (
    "Agregar producto",
    "Buscar producto",
    "Listar productos",
    "Calcular valor total del inventario",
    "Salir",
)


def _seleccionar_opcion(opciones: tuple[str, ...]) -> int:
    while True:
        print("     Menú principal")
        print(*(f"{i}. {texto}" for i,
              texto in enumerate(opciones, start=1)), sep="\n")
        try:
            opcion = int(input())
            if opcion in range(1, len(opciones) + 1):
                break
            print("Elige una de las opciones disponibles")
        except ValueError:
            print("La opción elegida debe ser un número")
    return opcion


def menu_principal(inventario: Inventario) -> None:
    while (opcion := _seleccionar_opcion(OPCIONES)) != len(OPCIONES):
        match opcion:
            case 1:
                _agregar_producto_pedido(inventario)
            case 2:
                _mostrar_producto_buscado(inventario)
            case 3:
                inventario.listar_productos()
            case 4:
                _mostrar_total_inventario(inventario)


if __name__ == "__main__":
    menu_principal(Inventario())
