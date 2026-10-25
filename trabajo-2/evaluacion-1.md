# Evaluación 1 del Trabajo 2: Programación Orientada a Objetos en Python

**Entrega:** [`sistema_inventario.py`](sistema_inventario.py)
**Resultado:** ¡Superado! (mínimo para superarlo: 5/10)

## Nota final: 9,85 / 10

| Criterio | Ponderación | Puntuación |
| :--- | :---: | :---: |
| Implementación de la clase Producto | 30% | 28,5 / 30 |
| Implementación de la clase Inventario | 30% | 30 / 30 |
| Manejo de excepciones | 20% | 20 / 20 |
| Interfaz de usuario y funcionalidad | 20% | 20 / 20 |

## Detalle por criterio

### 1. Implementación de la clase Producto (9,5/10)
La clase `Producto` cubre los atributos, métodos y validaciones principales requeridos. El único detalle relevante es que no valida explícitamente que `nombre` sea una cadena antes de procesarlo, aunque el flujo del menú sí proporciona texto. La lógica restante es clara y adecuada.

**Error detectado**
- El constructor aplica `strip()` a `nombre` antes de comprobar su tipo. Si se le pasa un valor que no sea una cadena, se produce un `AttributeError` en lugar de una validación controlada; es un fallo menor porque desde el menú el nombre siempre se lee como texto.

**Aspecto positivo**
- La clase implementa los métodos solicitados y comprueba que el precio sea numérico y no negativo, y que la cantidad sea un entero no negativo. También rechaza nombres vacíos y muestra la información del producto de forma legible.

### 2. Implementación de la clase Inventario (10/10)
La clase implementa las operaciones solicitadas y mantiene una colección de productos de forma sencilla. La búsqueda devuelve el producto encontrado o `None`, tal como se pide, y los métodos de cálculo y listado completan correctamente la funcionalidad.

**Aspecto positivo**
- `Inventario` inicializa una lista propia, verifica el tipo de los productos al agregarlos y ofrece búsqueda exacta sin distinguir mayúsculas y minúsculas. También calcula correctamente el valor total y muestra los productos, incluido el caso de inventario vacío.

### 3. Manejo de excepciones (10/10)
El manejo de errores cubre las entradas habituales del menú y las validaciones de precio y cantidad. La ausencia de un producto se resuelve mostrando un mensaje, respetando que la búsqueda devuelva `None` cuando no hay coincidencia. No se observan fallos relevantes en este criterio.

**Aspecto positivo**
- Se controlan las conversiones de precio, cantidad y opción del menú con bloques `try-except`. Al agregar, también se capturan los errores de validación para mostrar un mensaje y continuar; cuando una búsqueda no encuentra resultados, se informa al usuario sin interrumpir el programa.

### 4. Interfaz de usuario y funcionalidad (10/10)
La interfaz permite agregar, buscar y listar productos, así como consultar el valor total del inventario. El flujo de entrada y los mensajes cubren tanto las operaciones satisfactorias como los casos de datos inválidos o productos no encontrados. La aplicación se inicia correctamente desde la sección principal.

**Aspecto positivo**
- El menú ofrece las cuatro operaciones requeridas y la opción de salir, y se repite hasta que el usuario elige esta última. Las entradas numéricas inválidas o las opciones fuera de rango se vuelven a solicitar.

## Resumen global
La entrega presenta un sistema de inventario completo y organizado en torno a las clases `Producto` e `Inventario`, con las operaciones centrales implementadas. El menú permite probarlas de forma interactiva y el tratamiento de errores evita que las entradas habituales inválidas interrumpan el flujo. Como mejora concreta, conviene validar explícitamente el tipo de `nombre` en el constructor para que cualquier uso de la clase, también fuera del menú, produzca un error controlado.
