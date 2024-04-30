def estimate_price(mileage, theta0, theta1):
    res = theta0 + (theta1 * mileage)
    return res


if __name__ == "__main__":
    theta0 = 1
    theta1 = 2
    mileage = 3
    print(estimate_price(mileage, theta0, theta1))
