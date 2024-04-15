import pandas as pd


def human_traffic(data):
    df = pd.DataFrame(data)

    df = df.sort_values(by="id")

    df = df[df["people"] >= 100]

    df["lag_2"] = df["id"].shift(2).fillna(99).astype(int)
    df["lag_1"] = df["id"].shift(1).fillna(99).astype(int)
    df["lead_1"] = df["id"].shift(-1).fillna(99).astype(int)
    df["lead_2"] = df["id"].shift(-2).fillna(99).astype(int)

    df = df[((df["id"] - df["lag_1"] == 1) & (df["lead_1"] - df["id"] == 1)) | ((df["id"] - df["lag_2"] == 2) & (df["id"] - df["lag_1"] == 1)) | ((df["lead_2"] - df["id"] == 2) & (df["lead_1"] - df["id"] == 1))]
    print(df[["id", "visit_date", "people"]])


if __name__ == "__main__":
    data = {
        "id": [1,2,3,4,5,6,7,8],
        "visit_date": ["2017-01-01", "2017-01-02", "2017-01-03", "2017-01-04", "2017-01-05", "2017-01-06", "2017-01-07", "2017-01-09"],
        "people": [10, 109, 150, 99, 145, 1455, 199, 188]
    }

    human_traffic(data)
