menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar estudiante\n4. Salir"
subMenuNotas = "1.Parciales\n2.Quices\n3.Trabajos\n4.Regresar al menu principal"
hasError = True
def menuPrincipal() -> int:
    global hasError
    hasError = True
    print(menu)
    while (hasError == True):
        try:
            hasError = False
            return int(input(":)"))
        except ValueError:
            hasError = True