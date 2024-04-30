from getData import get_data
from predict import estimate_price as ep
from train import linear_regression
from graphics import graphics
from normalize import normalize, reverse_normalize


if __name__ == "__main__":
    data = get_data()
    # print(data)
    df, my_map = normalize(data)
    (theta0, theta1) = linear_regression(df)
    n_theta0 = reverse_normalize(theta0, my_map, "km")
    n_theta1 = reverse_normalize(theta1, my_map, "km")
    # print(f"theta0 = {n_theta0}\ntheta1 = {n_theta1}")
    graphics(df, theta0, theta1)
    while 1:
        km = input("enter a mileage: ")
        if km == "exit" or km == "quit":
            exit()
        elif km.isdigit():
            n_km = (int(km) - my_map['min_mileage']) / (my_map['max_mileage'] - my_map["min_mileage"])
            price = reverse_normalize(
                ep(n_km, theta0, theta1),
                my_map,
                "price"
            )
            print(f"estimated price for {km} as mileage is {price[0]}")
        else:
            print("enter an integer\n")
