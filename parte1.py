import csv


def lista_alumno_notas_y_asistencia():
    with open('calificaciones.csv', 'r') as f:
        reader = csv.reader(f)
        lista = []
+
