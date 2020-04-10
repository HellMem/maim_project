import pandas as pd
import numpy as np


def load_materias():
    for i in range(1, 2):
        path_asistencias = "data/asistencias/asistencias_{}.csv".format(i)
        path_examenes = "data/examenes/resultados_examenes_{}.csv".format(i)
        path_trabajos = "data/trabajos/resultados_trabajos_totales_{}.csv".format(i)

        asistencias = pd.read_csv(path_asistencias)
        resultados_examenes = pd.read_csv(path_examenes)
        resultados_trabajos = pd.read_csv(path_trabajos)

        for m in range(1, 55):
            nombre_materia = "X{}".format(m)
            asistencias_completas = len(asistencias[asistencias[nombre_materia] == 2])
            # Cada 2 retardos cuentan como falta
            retardos = len(asistencias[asistencias[nombre_materia] == 1])
            asistencias_completas = asistencias_completas - int(retardos / 2)
            porcentaje_asistencias = (asistencias_completas / 32) * 100
            print("porcentaje de asistencias para {}: {}".format(nombre_materia, porcentaje_asistencias))
            # Los exámenes representan el 40% de la calificación (la suma de ambos)
            suma_examenes = resultados_examenes[nombre_materia].sum(axis=0)
            print("suma examenes para {}: {}".format(nombre_materia, suma_examenes))
            # Los trabajos representan el 60% de la calificación (el promedio de todos los trabajos)
            porcentaje_trabajos = ((resultados_trabajos[nombre_materia].sum(axis=0) / 4) / 20) * 60
            print("resultado trabajos para {}: {}".format(nombre_materia, porcentaje_trabajos))
            print("resultado final para {}: {}".format(nombre_materia, (suma_examenes + porcentaje_trabajos)))
            print('-' * 500)


def load_perfil():
    perfiles = pd.read_csv("data/perfil_alumnos.csv")
    cambio_carrera = pd.read_csv("data/cambio_carrera.csv")
    distribucion_becas = pd.read_csv("data/distribucion_becas.csv")
    perfiles['cambio_carrera'] = cambio_carrera['x']
    perfiles['distribucion_becas'] = distribucion_becas['x']

    return perfiles


perfiles = load_perfil()
#load_materias()

print(perfiles)


