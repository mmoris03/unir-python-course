# Evaluación 1 del Trabajo 1: Sintaxis Python

**Entrega:** [`calculadora_promedios.py`](calculadora_promedios.py)
**Resultado:** ¡Superado! (mínimo para superarlo: 5/10)

## Nota final: 9,8 / 10

| Criterio | Ponderación | Puntuación |
| :--- | :---: | :---: |
| Implementación de funciones y estructura | 30% | 30 / 30 |
| Manejo de estructuras de datos | 25% | 25 / 25 |
| Cálculos y lógica | 25% | 25 / 25 |
| Validación de entrada y manejo de errores | 20% | 18 / 20 |

## Detalle por criterio

### 1. Implementación de funciones y estructura (10/10)
La estructura cumple lo pedido y las funciones tienen responsabilidades claras. La organización del programa facilita seguir la entrada de datos, el procesamiento y la presentación de resultados.

### 2. Manejo de estructuras de datos (10/10)
El uso de listas es adecuado para los datos solicitados y la indexación permite relacionar correctamente cada materia con su nota. También se recorren las parejas para mostrar el resumen final.

### 3. Cálculos y lógica (10/10)
Los cálculos y las comparaciones cumplen los requisitos: se clasifican las notas según el umbral y se identifican correctamente los extremos. El resumen muestra los resultados asociados a sus materias.

### 4. Validación de entrada y manejo de errores (9/10)
La validación de nombres, calificaciones y respuesta de continuidad es sólida.

**Error detectado**
- `ingresar_calificaciones` solicitaba obligatoriamente una primera materia antes de preguntar si se desea continuar, por lo que no se podía terminar la entrada sin introducir ninguna. Aunque `main` contempla ese caso, la rama no era alcanzable mediante el flujo normal del programa.

**Aspectos positivos**
- Se comprueba que el nombre no esté en blanco, se manejan notas que no se pueden convertir a número y se rechazan valores fuera del intervalo de 0 a 10.
- La respuesta para continuar también se valida hasta recibir una opción reconocida.

## Resumen global
La entrega resuelve de forma clara los requisitos principales: entrada validada, almacenamiento en listas, cálculos y resumen completo. Destaca la separación en funciones y el uso correcto de índices para relacionar notas con materias. La mejora más importante es permitir que el usuario termine sin introducir materias, para que el caso vacío contemplado en `main` pueda ocurrir realmente. También conviene tener presente que el promedio requiere una lista no vacía, condición que actualmente depende del flujo de entrada.
