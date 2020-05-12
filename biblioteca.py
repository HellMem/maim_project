import pandas as pd

def load_biblioteca(perfiles, num_of_students):
    # uso de la biblioteca
    # Alberto: Redondear. Uso físico y virtual. vector.
    lista_biblioteca = []
    for i in range(1, num_of_students+1):
        path_biblioteca = "data/biblioteca/uso_biblioteca_totales_{}.csv".format(i)

        uso_biblioteca = pd.read_csv(path_biblioteca)
        # Se redondean los datos, se elimina la columna de index (primera columna) y se suman todos los elementos de la matriz
        sum_uso_biblio = uso_biblioteca.round(0).to_numpy()[:,1:].sum()
        lista_biblioteca.append((sum_uso_biblio)/sum_uso_biblio.size)

    df = pd.Series(lista_biblioteca)
    perfiles['uso_biblioteca'] = df

    return perfiles

