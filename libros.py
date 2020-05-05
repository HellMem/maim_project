import pandas as pd

def load_pagos(perfiles, num_of_students):
    # No especificado, quiza el numero equivale al numero de libros apartados por cada materia
    lista_pagos = []
    for i in range(1, num_of_students+1):
        path_pagos = "data/apartadolibros/separacion_libros_totales_{}.csv".format(i)

        pagos = pd.read_csv(path_pagos)
        # Se elimina la columna de index (primera columna) y se suman todos los elementos de la matriz
        sum_pagos = pagos.to_numpy()[:, 1:].sum()
        lista_pagos.append(int(sum_pagos))

    df = pd.Series(lista_pagos)
    perfiles['libros'] = df

    return perfiles

