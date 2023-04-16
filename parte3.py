"""Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para
 aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes
  parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.
"""
import csv
with open('calificaciones.csv', encoding='utf-8-sig') as f:
    estudiante={}
    reader = f.readlines()
    lista = []
    for row in reader:
        estudiante["Apellidos"] = row[0]
        estudiante["Nombre"] = row[1]
        estudiante["Asistencia"] = row[2]
        estudiante["Parcial1"] = row[3]
        estudiante["Parcial2"] = row[4]
        estudiante["Ordinaria1"] = row[5]
        estudiante["Ordianria2"] = row[6]
        estudiante["Practicas"] = row[7]
        estudiante["PracticasOrdinaria"] = row[8]
    lista.append(estudiante)
    lista_ordenada = 1
    lista.pop(0)
    print(lista)
