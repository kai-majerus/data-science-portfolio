import numpy as np
from termcolor import colored

from src.DataPreparation import data_preprocessing
from src.metrics import mean_squared_error, r2_score


class LinearRegression:
    def __init__(self, lr=0.01, n_iter=1000, csv_path=None):
        # hyperparameters initialization
        self.lr = lr
        self.n_iter = n_iter
        self.csv_path = csv_path
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # parameter initialization
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iter):
            # prediction
            y_pred = self.predict(X)

            # computing the gradients
            dW = np.dot(X.T, (y_pred - y)) / n_samples
            db = np.sum(y_pred - y) / n_samples

            # updating the parameters
            self.weights -= self.lr * dW
            self.bias -= self.lr * db

    def predict(self, X):
        if self.weights is None:
            raise Exception("Model is not trained yet!")
        return np.dot(X, self.weights) + self.bias

    def LR_main(self):
        # Splitting data into train and test
        X_train, X_test, y_train, y_test = data_preprocessing(self.csv_path)

        # model fit and predict
        self.fit(X_train, y_train)
        linear_predict = self.predict(X_test)

        # Metrics
        print(
            colored(
                (f"MSE of Linear Model : {mean_squared_error(y_test, linear_predict)}"),
                "yellow",
            )
        )
        print(
            colored(
                (f"R2 Score of Linear Model : {r2_score(y_test, linear_predict)}"),
                "yellow",
            )
        )


if __name__ == "__main__":
    csv_path = "raw_data/EPL_Soccer_MLR_LR.csv"

    # lr = learning rate
    # n_iter = no. of iterations
    linear_model = LinearRegression(lr=0.00001, n_iter=100, csv_path=csv_path)
    linear_model.LR_main()
