import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_line_point(W):
    shape = np.shape(W)

def load_data():
    URL_= 'iris.data'
    data = pd.read_csv(URL_, header = None)

    # make the dataset linearly separable
    data = data[:100]

    data[4] = np.where(data.iloc[:, -1]=='Iris-setosa', 0, 1)
    print(data)
    data = np.asmatrix(data, dtype = 'float64')
    return data

data = load_data()

plt.scatter(np.array(data[:50,0]), np.array(data[:50,2]), marker='o', label='setosa')
plt.scatter(np.array(data[50:,0]), np.array(data[50:,2]), marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend()
plt.show()

def perceptron(data, num_iter):
    features = data[:, :-1]
    labels = data[:, -1]

    # set weights to zero
    w = np.zeros(shape=(1, features.shape[1]+1))
    misclassified_ = []
    counter = 0
    for epoch in range(num_iter):
        misclassified = 0
        for x, label in zip(features, labels):
            x = np.insert(x,0,1)
            y = np.dot(w, x.transpose())
            target = 1.0 if (y > 0) else 0.0
            delta = (label.item(0,0) - target)

            if(delta): # misclassified
                misclassified += 1
                w += (delta * x)
        misclassified_.append(misclassified)

    return (w, misclassified_)

num_iter = 10
w, misclassified_ = perceptron(data, num_iter)

epochs = np.arange(1, num_iter+1)
plt.plot(epochs, misclassified_)
plt.xlabel('iterations')
plt.ylabel('misclassified')


plt.show()
