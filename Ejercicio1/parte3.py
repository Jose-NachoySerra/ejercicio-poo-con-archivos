"""Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para
 aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes
  parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.
"""
import csv
with open('calificaciones.csv', 'r') as f:
    reader = csv.reader(f)
    lista = []
    for row in reader:
        lista.append(row)
    print(lista)
    