import matplotlib.pyplot as plt
import numpy as np

from getData import get_data


def graphics(data, theta0, theta1):
    # line of linear regression
    x = np.array(data['km']).reshape(-1, 1)
    y = np.array(data['price']).reshape(-1, 1)
    lr_y = theta0 + theta1 * x

    # plot
    fig, ax = plt.subplots()

    ax.plot(x, lr_y, linewidth=2.0)
    ax.scatter(x, y)

    plt.show()


if __name__ == "__main__":
    data = get_data()
    graphics(data, 8000, -5/240)
