def _pedir_materia() -> str:
    while not (materia := input("Nombre de la materia: ").strip()):
        print("El nombre de la materia no debe estar en blanco")

    return materia


def _pedir_calificacion() -> float:
    while True:
        try:
            calificacion = float(
                input("Calificación de la materia: ").replace(",", ".")
            )
        except ValueError:
            print("La calificación debe ser un número")
            continue  # pedir otro número

        if 0 <= calificacion <= 10:
            return calificacion
        print("La calificación debe estar entre 0 y 10")


def _preguntar_si_no(pregunta: str) -> bool:
    while True:
        match input(f"{pregunta} (s/n): ").strip().lower():
            case 's':
                return True
            case 'n':
                return False
            case _:
                print("Responde 's' o 'n'")


def ingresar_calificaciones() -> tuple[list[str], list[float]]:
    materias: list[str] = []
    calificaciones: list[float] = []

    while _preguntar_si_no("¿Quieres introducir una nota?"):
        materias.append(_pedir_materia())
        calificaciones.append(_pedir_calificacion())

    return materias, calificaciones


def calcular_promedio(calificaciones: list[float]) -> float:
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones: list[float], umbral: float = 5.0) -> tuple[list[int], list[int]]:
    aprobadas: list[int] = []
    reprobadas: list[int] = []

    for indice, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(indice)
        else:
            reprobadas.append(indice)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones: list[float]) -> tuple[int, int]:
    calificacion_mas_alta = calificacion_mas_baja = calificaciones[0]
    indice_nota_mas_alta = indice_nota_mas_baja = 0

    for indice, calificacion in enumerate(calificaciones):
        if calificacion > calificacion_mas_alta:
            calificacion_mas_alta = calificacion
            indice_nota_mas_alta = indice

        if calificacion < calificacion_mas_baja:
            calificacion_mas_baja = calificacion
            indice_nota_mas_baja = indice

    return indice_nota_mas_alta, indice_nota_mas_baja


def _mostrar_materias_y_calificaciones(materias: list[str], calificaciones: list[float]) -> None:
    print("CALIFICACIONES")
    for materia, calificacion in zip(materias, calificaciones):
        print(f"{materia} : {calificacion}")


def _mostrar_promedio_general(promedio: float) -> None:
    print(f"PROMEDIO GENERAL: {promedio:.2f}")


def _mostrar_materias_aprobadas(materias: list[str], aprobadas: list[int]) -> None:
    print("APROBADAS")
    print(
        ", ".join([materias[indice] for indice in aprobadas])
        if aprobadas
        else "Ninguna"
    )


def _mostrar_materias_reprobadas(materias: list[str], reprobadas: list[int]) -> None:
    print("REPROBADAS")
    print(
        ", ".join([materias[indice] for indice in reprobadas])
        if reprobadas
        else "Ninguna"
    )


def _mostrar_materia_mejor_calificacion(materias: list[str], calificaciones: list[float], indice_nota_mas_alta: int) -> None:
    print("MATERIA CON MEJOR CALIFICACION")
    print(
        f"{materias[indice_nota_mas_alta]} : {calificaciones[indice_nota_mas_alta]}"
    )


def _mostrar_materia_peor_calificacion(materias: list[str], calificaciones: list[float], indice_nota_mas_baja: int) -> None:
    print("MATERIA CON PEOR CALIFICACION")
    print(
        f"{materias[indice_nota_mas_baja]} : {calificaciones[indice_nota_mas_baja]}"
    )


def _mostrar_resumen(materias: list[str], calificaciones: list[float], promedio: float, aprobadas: list[int], reprobadas: list[int], indice_nota_mas_alta: int, indice_nota_mas_baja: int) -> None:
    sep = '-' * 30

    _mostrar_materias_y_calificaciones(materias, calificaciones)
    print(sep)
    _mostrar_promedio_general(promedio)
    print(sep)
    _mostrar_materias_aprobadas(materias, aprobadas)
    print(sep)
    _mostrar_materias_reprobadas(materias, reprobadas)
    print(sep)
    _mostrar_materia_mejor_calificacion(
        materias,
        calificaciones,
        indice_nota_mas_alta
    )
    print(sep)
    _mostrar_materia_peor_calificacion(
        materias,
        calificaciones,
        indice_nota_mas_baja
    )


def main() -> None:
    materias, calificaciones = ingresar_calificaciones()
    if not materias:
        print("No se ingresó ninguna materia.")
    else:
        promedio = calcular_promedio(calificaciones)
        aprobadas, reprobadas = determinar_estado(calificaciones)
        indice_nota_mas_alta, indice_nota_mas_baja = encontrar_extremos(
            calificaciones
        )
        _mostrar_resumen(
            materias,
            calificaciones,
            promedio,
            aprobadas,
            reprobadas,
            indice_nota_mas_alta,
            indice_nota_mas_baja
        )
    print("¡Hasta luego!")


if __name__ == "__main__":
    main()
