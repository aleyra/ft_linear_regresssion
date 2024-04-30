import copy

from getData import get_data


def normalize(data):
    max_mileage = data[['km']].stack().max()
    min_mileage = data[['km']].stack().min()
    max_price = data[['price']].stack().max()
    min_price = data[['price']].stack().min()

    df = copy.deepcopy(data)

    df[['km']] = (df[['km']] - min_mileage) / (max_mileage - min_mileage)
    df[['price']] = (df[['price']] - min_price) / (max_price - min_price)
    my_map = {
        'max_mileage': max_mileage,
        'min_mileage': min_mileage,
        'max_price': max_price,
        'min_price': min_price
    }
    return (df, my_map)


def reverse_normalize(n, my_map, what):
    max = 1
    min = 0
    if what == "km":
        max = my_map["max_mileage"]
        min = my_map["min_mileage"]
    else:
        max = my_map['max_price']
        min = my_map['min_price']
    d = n * (max - min) + min
    return d


if __name__ == "__main__":
    df = get_data()
    print(df)
    n_df, my_map = normalize(df)
    print(n_df)
    res = reverse_normalize(0.935345, my_map, "price")
    print(res)
