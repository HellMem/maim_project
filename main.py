from student_data_reader import load_perfil
from student_data_reader import load_materias
from student_data_reader import plot_elbow
from pagos import load_pagos

# Numero de estudiantes que se obtendrán del dataset, max = 1000
NUM_OF_STUDENTS = 2

perfiles = load_perfil(NUM_OF_STUDENTS)
# perfiles = load_materias()
perfiles = load_pagos(perfiles, NUM_OF_STUDENTS)

plot_elbow(perfiles)
