from student_data_reader import load_perfil
from student_data_reader import load_materias
from student_data_reader import plot_elbow
from pagos import load_pagos
from libros import load_libros
from biblioteca import load_biblioteca
from plataforma import load_plataforma

# Numero de estudiantes que se obtendrán del dataset, max = 1000
NUM_OF_STUDENTS = 1000

perfiles = load_perfil(NUM_OF_STUDENTS)

# perfiles = load_materias()
perfiles = load_pagos(perfiles, NUM_OF_STUDENTS)
perfiles = load_libros(perfiles, NUM_OF_STUDENTS)
perfiles = load_biblioteca(perfiles, NUM_OF_STUDENTS)
perfiles = load_plataforma(perfiles, NUM_OF_STUDENTS)


plot_elbow(perfiles)
