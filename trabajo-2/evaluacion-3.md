# Evaluación 3 del Trabajo 2: Programación Orientada a Objetos en Python

**Entrega:** [`sistema_inventario.py`](sistema_inventario.py)
**Resultado:** ¡Superado! (mínimo para superarlo: 5/10)

## Nota final: 10 / 10

| Criterio | Ponderación | Puntuación |
| :--- | :---: | :---: |
| Implementación de la clase Producto | 30% | 30 / 30 |
| Implementación de la clase Inventario | 30% | 30 / 30 |
| Manejo de excepciones | 20% | 20 / 20 |
| Interfaz de usuario y funcionalidad | 20% | 20 / 20 |

## Detalle por criterio

### 1. Implementación de la clase Producto (10/10)
La clase `Producto` incluye todos los atributos y métodos solicitados, con validaciones adecuadas para los tipos y los valores. Además, normaliza el precio a `float` y excluye los booleanos de las validaciones numéricas. Cumple el criterio sin fallos relevantes.

**Aspecto positivo**
- La clase valida que el nombre sea texto no vacío, que el precio sea numérico y no negativo, y que la cantidad sea un entero no negativo. También implementa las actualizaciones, el cálculo del valor total y una representación legible con `__str__`.

### 2. Implementación de la clase Inventario (10/10)
La clase reúne correctamente las operaciones requeridas para gestionar productos: añadir, buscar, calcular el valor total y listar. La búsqueda devuelve el producto correspondiente o `None`, y el cálculo y el listado contemplan el inventario vacío. La implementación cumple el criterio.

**Aspectos positivos**
- `Inventario` inicializa su propia lista, comprueba que los elementos añadidos sean objetos `Producto` y realiza la búsqueda exacta sin distinguir mayúsculas y minúsculas.
- El cálculo suma correctamente el valor de cada producto y el listado presenta los productos o informa cuando el inventario está vacío.

### 3. Manejo de excepciones (10/10)
El programa maneja adecuadamente las conversiones inválidas y las excepciones por valores o tipos no admitidos al crear productos. Las cantidades negativas y los nombres vacíos se comunican de forma controlada. También se informa de los productos no encontrados sin provocar una interrupción.

**Aspectos positivos**
- Se controlan los errores de conversión de precio, cantidad y opción del menú, y se capturan los errores de validación al crear un producto para informar al usuario sin interrumpir el menú.
- Cuando la búsqueda no encuentra coincidencias, la interfaz muestra un mensaje y continúa, respetando que `buscar_producto` devuelva `None`.

### 4. Interfaz de usuario y funcionalidad (10/10)
La interfaz ofrece todas las operaciones solicitadas y presenta los resultados y errores por consola. Las entradas numéricas incorrectas y las opciones fuera de rango se gestionan sin abandonar el menú. El flujo de inicio y salida está correctamente conectado.

**Aspectos positivos**
- El menú permite agregar, buscar y listar productos, consultar el valor total y salir; además, repite el ciclo hasta seleccionar la opción de salida.
- La sección principal instancia `Inventario` y lo proporciona al menú, conectando correctamente la aplicación con las operaciones implementadas.

## Resumen global
Has construido un sistema de inventario completo y bien organizado, con clases que cubren las operaciones centrales y validaciones sólidas. El menú permite probarlas de forma interactiva y gestiona adecuadamente las entradas inválidas y las búsquedas sin resultados. No se aprecian carencias relevantes respecto a los requisitos evaluados.
