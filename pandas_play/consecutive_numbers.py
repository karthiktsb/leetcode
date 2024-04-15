import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:

    def shifts(data):
        data["prev"] = data["id"].shift(1).fillna(99).astype(int)
        data["next"] = data["id"].shift(-1).fillna(99).astype(int)
        return data

    logs = logs.sort_values(by=["num", "id"])

    grouped = logs.groupby("num").apply(shifts).reset_index(drop=True)

    filtered = grouped[(grouped["id"] - grouped["prev"] == 1) & (grouped["next"] - grouped["id"] == 1)]

    print(filtered[["num"]].drop_duplicates())


def consecutive_numbers_join(logs: pd.DataFrame) -> pd.DataFrame:

    logs["prev"] = logs["id"] - 1
    logs["next"] = logs["id"] + 1

    merged = logs.merge(logs, left_on=["num", "prev"], right_on=["num", "id"])
    merged1 = merged.merge(logs, left_on=["num", "next_x"], right_on=["num", "id"])

    print(merged1["num"].drop_duplicates())



data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "num": [1, 1, 1, 2, 1, 2, 4, 2, 3, 3]
}

consecutive_numbers(pd.DataFrame(data))
consecutive_numbers_join(pd.DataFrame(data))