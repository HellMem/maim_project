from student_data_reader import *
from nn_benchmark import *
from pagos import load_pagos
from libros import load_libros
from biblioteca import load_biblioteca
from plataforma import load_plataforma
from joblib import dump, load
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

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

# Using Pearson Correlation
plt.figure(figsize=(12, 10))
cor = perfiles.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()
# Correlation with assistance
# correlated features with "asistencia"are not efective for the model accuracy
# cor_target = abs(cor["asistencia"])
cor_target = abs(cor["nota_conducta"])
# Selecting highly correlated features
relevant_features = list(cor_target[cor_target > 0.5].index.values)
# perfiles_dataset = perfiles[relevant_features]
perfiles_dataset = perfiles

# Split dataset in train and test sets
X_train, X_test = train_test_split(perfiles_dataset, test_size=0.1, random_state=12345)

# Get best n of clusters using kmeans and add its cluster for each student
best_n = get_elbow(X_train, plot=True)

# Separate X and Y from trainset
y_train = X_train['cluster']
X_train.drop(columns='cluster', inplace=True)

# Train NN classification model
nn_model = get_nn_model(X_train, y_train, (5, 2))
pred_train_y = nn_model.predict(X_train)
print("Train report")
print(classification_report(y_train, pred_train_y))

# Save trained model
dump(nn_model, 'trained_model.joblib')

# Predict class for test set using trained NN model
pred_test_y = nn_model.predict(X_test)

# Separate students with churn risk, cluster 1 means that the student is in risk
# due to low highschool grades, grade and use of resources
students_in_risk = X_test[pred_test_y == 1]

students_in_risk.to_csv("output/risk.csv")