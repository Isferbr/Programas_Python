import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta*(target - self.predict(xi))
                self.w_[1:] += update*xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors.append(errors)

        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self,x):
        return np.where(self.net_input(x) >= 0.0, 1, -1)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data', header=None)
X = df.iloc[:,].values
y = df.iloc[:,1].values
#y = np.where(y == 'M',-1,1)

plt.scatter(X, color = 'blue', marker = 'o', label = 'diagnostic')
plt.xlabel('Maligno')
plt.ylabel('Beligno')
plt.legend(loc = 'upper left')
plt.show()

ppn = Perceptron(eta = 0.1, n_iter = 10)
ppn.fit(X, y)

plt.plot(range(1, len(ppn.errors) + 1), ppn.errors)

plt.xlabel('Attempts')
plt.ylabel('Number of misclassification')
plt.show()
