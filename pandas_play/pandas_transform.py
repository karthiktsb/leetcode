import pandas as pd
import numpy as np


def apply_func(df):
    df.sort_values(["mark"])
    df["prev"] = df["mark"].shift(1)
    df["next"] = df["mark"].shift(-1)

    return df


def main():
    df = pd.read_csv("student.csv")
    tdf = df
    # Transform NaN values
    df["mark"] = df["mark"].fillna(0)
    print(df)

    # If condition
    df["is_millenial"] = np.where(df["year"] >= 1983, "Yes", "No")
    print(df)

    # Case when clause
    conditions = [
            ((df["year"] == 1983) & (df["gender"] == "male")),
            ((df["year"] == 1983) & (df["gender"] == "female")),
            (df["year"] == 1984),  # Year is 1983
            (df["year"] >= 1985)  # Year is >= 1984
        ]

    values = ["AB","AG", "B", "C"]

    df["based_on_year"] = np.select(conditions, values, default="U")
    print(df)

    # String functions
    df["name_class"] = df["name"] + " - " + df["class"]
    df["starts_with_j"] = df["name"].str.rfind("i")
    df["skip_first_2"] = df["name"].str[2:]
    print(df[["name", "class", "name_class", "starts_with_j", "skip_first_2"]])

    # Numeric functions
    avg = sum(df["mark"]) / len(df)
    df["above_avg"] = df["mark"] - avg
    print(df[["mark", "above_avg"]])

    # Date Functions
    data = {'datetime': ['2024-01-01 08:30:00', '2025-03-01 10:45:00', '2025-04-01 15:00:00'],
            'value': [10, 20, 30]}
    ddf = pd.DataFrame(data)

    print(ddf)
    ddf["datetime"] = pd.to_datetime(ddf["datetime"])
    ddf["date"] = ddf["datetime"].dt.date
    ddf["prev_date"] = ddf["date"] - pd.Timedelta(days=1)
    ddf["diff"] = ddf["date"] - ddf["prev_date"]
    ddf["diff"] = pd.to_timedelta(ddf["diff"]).dt.days
    ddf["timediff"] = ddf["datetime"].diff().dt.days
    ddf["prev_time"] = ddf["datetime"].shift(1)
    ddf["diff_in_months"] = (ddf["datetime"].dt.year - ddf["prev_time"].dt.year) * 12 + (ddf["datetime"].dt.month - ddf["prev_time"].dt.month)
    with pd.option_context("display.max_columns", None):
        print(ddf)

    print("--------------")
    # Apply function - Can add multiple columns
    print(tdf[["year", "mark"]].groupby("year").apply(apply_func).reset_index(drop=True))
    print("--------------")
    print(tdf[["year", "name", "class"]].groupby("year").apply(
        lambda x: list(zip(x["name"], x["class"]))
    ))

    print("--------------")
    # Transform only does one column at a time
    tdf.sort_values(["year", "mark"], inplace=True)
    tdf["prev"] = tdf.groupby("year")["mark"].transform(lambda x: x.shift(1))
    print(tdf[["year", "mark", "prev"]])



main()