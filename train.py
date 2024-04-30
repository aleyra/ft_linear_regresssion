import pandas as pd
import numpy as np

from predict import estimate_price as ep
from getData import get_data


def linear_regression(data):
    mileage = np.array(data['km']).reshape(-1, 1)
    price = np.array(data['price']).reshape(-1, 1)

    theta0 = 0
    theta1 = 0
    learningRate = 0.7  # set manually
    m = data.shape[0]

    max_iter = 1000  # set manually, usually to 1000

    for j in range(max_iter):
        tmpth0 = 0
        for i in range(0, m):
            tmpth0 += ep(mileage[i], theta0, theta1) - price[i]
        tmpth0 = learningRate * (1 / m) * tmpth0

        tmpth1 = 0
        for i in range(0, m):
            tmpth1 += (ep(mileage[i], theta0, theta1) - price[i]) * mileage[i]
        tmpth1 = learningRate * (1 / m) * tmpth1

        theta0 -= tmpth0
        theta1 -= tmpth1

    return (theta0, theta1)


if __name__ == "__main__":
    data = get_data()
    linear_regression(data)
