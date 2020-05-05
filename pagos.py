import pandas as pd

def load_pagos(perfiles, num_of_students):
    # 2 en tiempo, 1 retraso, 0 no pago
    lista_pagos = []
    for i in range(1, num_of_students+1):
        path_pagos = "data/registropagos/registro_pagos_{}.csv".format(i)

        pagos = pd.read_csv(path_pagos)
        # Se elimina la columna de index (primera columna) y se suman todos los elementos de la matriz
        sum_pagos = pagos.to_numpy()[:,1:].sum()
        lista_pagos.append(int(sum_pagos))

    df = pd.Series(lista_pagos)
    perfiles['pagos'] = df

    return perfiles

