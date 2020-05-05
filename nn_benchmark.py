from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from student_data_reader import *

def plot_elbow(data):
    sse = {}
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, max_iter=1000).fit(data)
        data["clusters"] = kmeans.labels_
        sse[k] = kmeans.inertia_ # Inertia: Sum of distances of samples to their closest cluster center
    plt.figure()
    plt.plot(list(sse.keys()), list(sse.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("SSE")
    plt.show()



def get_kmeans_model(data, clusters):
    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(data)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    print(labels)
    print(centers)

    return kmeans


def get_nn_model(data, labels, layer_size):
    clf = MLPClassifier(solver='adam', alpha=0.001, hidden_layer_sizes=layer_size, random_state=1)
    return clf.fit(data, labels)


if __name__ == "__main__":
    perfiles = load_perfil(500)
    model = get_kmeans_model(perfiles, 2)

    X_train, X_test, y_train, y_test = train_test_split(perfiles.values, model.labels_, test_size=0.20, random_state=42)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    parameter_space = {
        'hidden_layer_sizes': [(5, 2), (6, 2), (7, 2), (8, 2), (9, 2)],
        'alpha': [0.001, 0.003, 0.01, 0.03, 0.1, 0.3],
        'activation': ['tanh', 'relu'],
        'learning_rate': ['constant', 'adaptive']
    }

    nn_model = get_nn_model(X_train, y_train, (5, 2))

    pred_train_y = nn_model.predict(X_train)
    print("Train report")
    print(classification_report(y_train, pred_train_y))

    print('-' * 100)

    pred_test_y = nn_model.predict(X_test)
    print("Test report")
    print(classification_report(y_test, pred_test_y))
