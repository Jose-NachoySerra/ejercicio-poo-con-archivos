import csv
def lista_alumno_notas_y_asistencia():
    with open('calificaciones.csv', 'r') as f:
        reader = csv.reader(f)
        lista = []
        for row in reader:
            lista.append(row)
        lista.pop(0)
        lista_ordenada = sorted(lista, key=lambda x: x[0])
        return lista_ordenada
print(lista_alumno_notas_y_asistencia())

