import pandas as pd
import numpy as np


def load_data():
    perfil = pd.read_csv("data/perfil_alumnos.csv")
    print(perfil)



load_data()