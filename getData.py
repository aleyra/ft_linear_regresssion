import pandas as pd


def get_data():
    data = pd.read_csv("data.csv")
    return data


if __name__ == "__main__":
    data = get_data()
    print(data.shape)
