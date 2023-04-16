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

def calcular_nota_final(lista):
    for alumno in lista:
        parcial_teorico1 = float(alumno['parcial_teorico1'])
        parcial_teorico2 = float(alumno['parcial_teorico2'])
        parcial_practico = float(alumno['parcial_practico'])

        nota_teorico1 = parcial_teorico1 * 0.3
        nota_teorico2 = parcial_teorico2 * 0.3
        nota_practico = parcial_practico * 0.4
        nota_final = nota_teorico1 + nota_teorico2 + nota_practico