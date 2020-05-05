import pandas as pd

def load_libros(perfiles, num_of_students):
    # No especificado, quiza el numero equivale al numero de libros apartados por cada materia
    lista_libros = []
    for i in range(1, num_of_students+1):
        path_libros = "data/apartadolibros/separacion_libros_totales_{}.csv".format(i)

        libros = pd.read_csv(path_libros)
        # Se elimina la columna de index (primera columna) y se suman todos los elementos de la matriz
        sum_libros = libros.to_numpy()[:, 1:].sum()
        lista_libros.append(int(sum_libros))

    df = pd.Series(lista_libros)
    perfiles['libros'] = df

    return perfiles

