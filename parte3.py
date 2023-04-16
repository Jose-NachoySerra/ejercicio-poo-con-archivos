"""Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para
 aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes
  parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.
"""
import csv
with open("calificaciones.csv", encoding="utf-8-sig") as f:
    
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
    
def alumnoAprobado(lista):
    aprobados = []
    suspensos = []
    for i in lista:
        if i["Parcial1"] == "":
            i["Parcial1"] = 0
        
        for x in i["Asistencia"]:
            if x== "%":
                i["Asistencia"] = i["Asistencia"].replace(x, "")
        for x in i["Parcial1"]:
            if x== ",":
                i["Parcial1"] = i["Parcial1"].replace(x, ".")
        for x in i["Parcial2"]:
            if x==",":
                i["Parcial2"] = i["Parcial2"].replace(x, ".")
        for x in i["Ordinaria1"]:
            if x==",":
                i["Ordinaria1"] = i["Ordinaria1"].replace(x, ".")
        for x in i["Ordianria2"]:
            if x==",":
                i["Ordianria2"] = i["Ordianria2"].replace(x, ".")
        for x in i["Practicas"]:
            if x==",":
                i["Practicas"] = i["Practicas"].replace(x, ".")
        for x in i["PracticasOrdinaria"]:
            if x==",":
                i["PracticasOrdinaria"] = i["PracticasOrdinaria"].replace(x, ".")

        if int(i["Asistencia"]) >= 75 and float(i["Parcial1"]) >= 4 and float(i["Parcial2"]) >= 4 and float(i["Ordinaria1"]) >= 4 and float(i["Ordianria2"]) >= 4 and float(i["Practicas"]) >= 4 and float(i["PracticasOrdinaria"]) >= 4:
            aprobados.append(i)
        else:
            suspensos.append(i)
    return aprobados, suspensos
print(alumnoAprobado(lista))