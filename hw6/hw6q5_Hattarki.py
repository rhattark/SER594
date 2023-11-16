from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import random
from collections import Counter

__author__ = "Rhishabh Suhas Hattarki"
__date__ = "20 November 2023"
__assignment = "SER594: Homework 6 Q5 Programming"

def euclidean_distance(first, second):
    return np.linalg.norm(first - second)

def knn_numpy(y_train, y_test, x_train, x_test, k = 4, tests=30):
    """
    See homework assignment.
    :param y_train: label training set
    :param y_test: label test set
    :param x_train: x training set
    :param x_test: x test set
    :param k: Number of neighbors.
    :param tests: Number of samples (start at index 0) to use when computing accuracy.
    :return:
    """
    
    predictions = []
    
    for i in range(tests):
        dist_from_train_pts = [(euclidean_distance(x_test[i], train_pt), idx) for idx, train_pt in enumerate(x_train)]
        closest_k_points = sorted(dist_from_train_pts, key=lambda x : x[0])[:k]
        closest_dist = closest_k_points[0][0]
        top_closest_labels = Counter([y_train[idx] for dist, idx in closest_k_points if dist == closest_dist])
        most_frequent_labels = top_closest_labels.most_common(2)
        if len(most_frequent_labels) == 1:
            predictions.append(most_frequent_labels[0][0])
        else:
            predictions.append(random.choice(most_frequent_labels)[0][0])
    
    accuracy = accuracy_score(y_test[:tests], predictions) * 100
    print(f'Manual Accuracy: {accuracy}%')


def knn_sklearn(y_train, y_test, x_train, x_test, k = 4, tests=30):
    """
    See previous.
    """
    
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test[:tests])
    accuracy = accuracy_score(y_test[:tests], y_pred) * 100
    print(f'Sklearn Accuracy: {accuracy}%')


# displays a digit using matplotlib. not needed for assignment, just provided for messing around.
def display_digit(x):
    import matplotlib.pyplot as plt
    x = x.reshape((28, 28))
    plt.imshow(x, cmap='gray')
    plt.show()


if __name__ == '__main__':

    # load MNIST data from numpy formatted files.
    with np.load('mnist.npz') as f:
        x_train, y_train = f['x_train'], f['y_train']
        x_test, y_test = f['x_test'], f['y_test']

    # convert sample points from 2D arrays to points/vectors
    x_train = x_train.reshape(-1, 784)
    x_test = x_test.reshape(-1, 784)

    print(f"Used {len(x_train)} samples for training.")

    # example usage of display_digit()
    # display_digit(x_train[0])

    knn_numpy(y_train, y_test, x_train, x_test)
    knn_sklearn(y_train, y_test, x_train, x_test)