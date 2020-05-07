import pandas as pd

def load_plataforma(perfiles, num_of_students):
    # No especificado, quiza el numero de horas que ha estado en la plataforma por materia
    # Alberto: Redondear, vector.
    lista_plataforma = []
    for i in range(1, num_of_students+1):
        path_plataforma = "data/apartadolibros/separacion_libros_totales_{}.csv".format(i)

        plataforma = pd.read_csv(path_plataforma)
        # Se redondean los datos, se elimina la columna de index (primera columna) y se suman todos los elementos de la matriz
        sum_plataforma = plataforma.round(0).to_numpy()[:, 1:].sum()
        lista_plataforma.append(int(sum_plataforma))

    df = pd.Series(lista_plataforma)
    perfiles['plataforma'] = df

    return perfiles

