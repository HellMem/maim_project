from student_data_reader import load_perfil
from student_data_reader import load_materias
from nn_benchmark import *
from pagos import load_pagos
from libros import load_libros
from biblioteca import load_biblioteca
from plataforma import load_plataforma
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso


# Numero de estudiantes que se obtendrán del dataset, max = 1000
NUM_OF_STUDENTS = 1000

perfiles = load_perfil(NUM_OF_STUDENTS)

perfiles = load_materias(perfiles, NUM_OF_STUDENTS)
perfiles = load_pagos(perfiles, NUM_OF_STUDENTS)
perfiles = load_libros(perfiles, NUM_OF_STUDENTS)
perfiles = load_biblioteca(perfiles, NUM_OF_STUDENTS)
perfiles = load_plataforma(perfiles, NUM_OF_STUDENTS)

# Delete student id
perfiles.drop(columns='id', inplace=True)

#Using Pearson Correlation
plt.figure(figsize=(12,10))
cor = perfiles.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()

# Split dataset in train and test sets
X_train, X_test = train_test_split(perfiles, test_size=0.1, random_state=12345)

# Get best n of clusters using kmeans and add its cluster for each student
best_n = get_elbow(X_train, plot=False)

# Separate X and Y from trainset
y_train = X_train['cluster']
X_train.drop(columns='cluster', inplace=True)

# Train NN classification model
nn_model = get_nn_model(X_train, y_train, (5, 2))

# Predict class for test set using trained NN model
pred_test_y = nn_model.predict(X_test)

# TODO: Separate students with churn risk, which is which?
X_test[pred_test_y==1]

# TODO: genetic algorithm is R?

print()