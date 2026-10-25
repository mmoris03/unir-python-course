# Evaluación 2 del Trabajo 2: Programación Orientada a Objetos en Python

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
La clase cumple los métodos y validaciones principales solicitados. El único fallo es un caso límite de tipado: `True` puede aceptarse como precio o cantidad por la relación entre `bool` e `int` en Python. El resto de la implementación es claro y funcional.

**Error detectado**
- Las validaciones con `isinstance(..., int)` también aceptan valores booleanos, porque en Python `bool` es una subclase de `int`. Así, `True` puede acabar registrado como precio o cantidad, aunque no sea un dato válido para esos atributos. Es un caso límite que no afecta al flujo normal del menú.

**Sugerencia de mejora**
- Como mejora opcional, puedes normalizar el precio aceptado a `float` para que el atributo conserve ese tipo incluso cuando se construye el producto con un entero. No afecta de forma relevante a la nota.

**Aspecto positivo**
- La clase valida que el nombre sea texto no vacío, que el precio no sea negativo y que la cantidad sea un entero no negativo. Implementa los dos métodos de actualización, el cálculo del valor total y una representación legible con `__str__`.

### 2. Implementación de la clase Inventario (10/10)
La clase implementa todas las operaciones pedidas y las integra de forma sencilla. La búsqueda devuelve el producto correspondiente o `None` si no hay coincidencia, y tanto el cálculo como el listado cubren también el caso de inventario vacío.

**Aspectos positivos**
- `Inventario` mantiene su propia lista, comprueba que los elementos añadidos sean objetos `Producto` y busca nombres sin distinguir mayúsculas y minúsculas.
- El cálculo suma correctamente el valor de cada producto y el listado presenta los productos o informa cuando el inventario está vacío.

### 3. Manejo de excepciones (10/10)
El flujo interactivo maneja adecuadamente las entradas numéricas inválidas y las excepciones de validación de productos. Los valores negativos y los nombres vacíos se comunican al usuario sin detener el menú. La búsqueda sin coincidencias también se resuelve de forma controlada.

**Aspectos positivos**
- Se controlan los errores de conversión de precio, cantidad y opción del menú, y los errores de validación al crear un producto se muestran sin interrumpir la aplicación.
- Cuando la búsqueda no encuentra el producto, la interfaz informa al usuario y continúa; esto respeta el contrato de devolver `None`.

### 4. Interfaz de usuario y funcionalidad (10/10)
La interfaz permite probar todas las operaciones del inventario y mantiene el ciclo del menú hasta seleccionar la salida. Las opciones inválidas se vuelven a solicitar y las operaciones presentan mensajes adecuados. La aplicación se inicia desde la sección principal.

**Aspectos positivos**
- El menú ofrece las cuatro operaciones solicitadas y la opción de salir, y se repite hasta que el usuario elige esta última.
- La sección principal crea un `Inventario` y lo pasa al menú. La interfaz permite agregar, buscar, listar y consultar el valor total, mostrando resultados y mensajes de error por consola.

## Resumen global
Has construido un sistema de inventario completo, con las clases y operaciones centrales bien organizadas y conectadas a un menú funcional. Destacan la búsqueda insensible a mayúsculas, el control de las conversiones de entrada y la gestión del inventario vacío. Como detalle menor, las validaciones de `Producto` aceptan `True` como precio o cantidad por el comportamiento de los booleanos en Python. En conjunto, la entrega cumple de forma sólida los requisitos.
