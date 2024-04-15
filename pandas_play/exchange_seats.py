import numpy as np
import pandas as pd


def exchange_seat(data):
    df = pd.DataFrame(data)
    df["seat"] = np.where(df["id"] % 2 == 1, np.where(df["student"].shift(-1), df["student"].shift(-1), df["student"]), df["student"].shift(1))
    df = df[["id", "seat"]]
    print(df.rename(columns={"seat": "student"}))


data = {
    "id": [1,2,3,4,5],
    "student": ["Abbot", "Doris", "Emerson", "Green", "Jeames"]
}

exchange_seat(data)
