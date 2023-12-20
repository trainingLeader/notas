import os
def addGrade(alumno : dict,categoria : str):
    dataNota = alumno.get("notas")
    evaluacion = dataNota.get(categoria)
    nota = float(input(f"Ingrese la nota de {alumno.get("nombre").upper()} :"))
    evaluacion.append(nota)
