"""Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para
 aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes
  parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.
"""
import csv
with open('calificaciones.csv', encoding='utf-8-sig') as f:
    
    reader = f.readlines()
    lista = []
    for row in reader:
        palabra = row.split(";")
        estudiante={}
        estudiante["Apellidos"] = palabra[0]
        estudiante["Nombre"] = palabra[1]
        estudiante["Asistencia"] = palabra[2]
        estudiante["Parcial1"] = palabra[3]
        estudiante["Parcial2"] = palabra[4]
        estudiante["Ordinaria1"] = palabra[5]
        estudiante["Ordianria2"] = palabra[6]
        estudiante["Practicas"] = palabra[7]
        estudiante["PracticasOrdinaria"] = palabra[8]
        lista.append(estudiante)
    
    lista.pop(0)
    print(lista)
