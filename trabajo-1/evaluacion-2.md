# Evaluación 2 del Trabajo 1: Sintaxis Python

**Entrega:** [`calculadora_promedios.py`](calculadora_promedios.py)
**Resultado:** ¡Superado! (mínimo para superarlo: 5/10)

## Nota final: 10 / 10

| Criterio | Ponderación | Puntuación |
| :--- | :---: | :---: |
| Implementación de funciones y estructura | 30% | 30 / 30 |
| Manejo de estructuras de datos | 25% | 25 / 25 |
| Cálculos y lógica | 25% | 25 / 25 |
| Validación de entrada y manejo de errores | 20% | 20 / 20 |

## Detalle por criterio

### 1. Implementación de funciones y estructura (10/10)
La estructura cumple los requisitos y separa con claridad las distintas responsabilidades. Las funciones solicitadas tienen los parámetros y resultados esperados, y el caso sin materias se comprueba antes de calcular o buscar extremos.

### 2. Manejo de estructuras de datos (10/10)
El uso de listas es adecuado y la relación entre cada materia y su calificación se conserva al agregarlas. La clasificación trabaja con índices, que después se utilizan correctamente para acceder a las materias; además, `zip` permite mostrar juntas las materias y sus notas.

### 3. Cálculos y lógica (10/10)
Los cálculos y las comparaciones corresponden a lo solicitado. El resumen muestra el promedio, las materias aprobadas y reprobadas y las materias asociadas a las notas más alta y más baja. El flujo principal evita invocar las funciones que requieren notas cuando no se ha introducido ninguna.

### 4. Validación de entrada y manejo de errores (10/10)
La validación cubre las entradas solicitadas y evita que una respuesta no reconocida interrumpa el flujo. El caso de listas vacías se maneja en `main`, por lo que no se calcula un promedio ni se buscan extremos sin datos. No se aprecian fallos relevantes en este criterio.

## Resumen global
La entrega resuelve de forma completa los requisitos principales: entrada validada, listas paralelas, cálculos correctos y un resumen final claro. Destaca la separación del código en funciones pequeñas y el uso coherente de índices para relacionar notas con materias. También se contempla correctamente que el usuario termine sin introducir ninguna materia. No se observan mejoras necesarias para cumplir los criterios evaluados.
