import pandas as pd


def second_higest(data):
    df = pd.DataFrame(data)

    df["SecondHighestSalary"] = df["salary"]
    df["rank"] = df["SecondHighestSalary"].rank(method="dense")

    print(df[df["rank"] == 2]["SecondHighestSalary"].to_dict().get(1, "null"))


if __name__ == "__main__":

    data = {
        "id": [1, 2, 3],
        "salary": [100, 200, 300]
    }

    data1 = {
        "id": [1],
        "salary": [100]
    }

    second_higest(data)
    second_higest(data1)




