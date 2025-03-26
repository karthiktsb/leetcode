import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:

    def shifts(data):
        data["curr"] = data["id"]
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

def shifts(data):
    data["prev"] = data["id"].shift(1).fillna(99).astype(int)
    data["next"] = data["id"].shift(-1).fillna(99).astype(int)
    return data

data = {
    "id": [1, 1, 2, 2,  3, 4, 5, 6, 7, 8, 9, 10],
    "num": [1, 2, 1, 4, 1, 2, 1, 2, 4, 2, 3, 3]
}

#consecutive_numbers(pd.DataFrame(data))
#consecutive_numbers_join(pd.DataFrame(data))

df = pd.DataFrame(data)

df.sort_values(by=["id", "num"], ascending=[True, True])
grouped_df = df.groupby("id")
df["rank"] = grouped_df["num"].rank(method='dense', ascending=True).astype(int)
df["row_number"] = grouped_df["num"].rank(method='first', ascending=True).astype(int)
df["lag"] = grouped_df["num"].shift(1).fillna(0).astype(int)
df["lead"] = grouped_df["num"].shift(-1).fillna(0).astype(int)
df["cumsum"] = grouped_df["num"].cumsum()


data1 = {
    "id": [1, 2, 3, 4, 5],
    "num1": [10, 20, 30, 40, 50],
    "num2": [15, 25, 35, 45, 55]
}

data2 = {
    "id": [2, 3, 4, 5, 6],
    "num1": [10, 20, 30, 40, 50],
    "num2": [15, 25, 35, 45, 55]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)



#df["prev"] = df["num"].shift(-1).fillna(99).astype(int)

print(df)
df1 = grouped_df["num"].sum()

print(df1)

data = {
    "id": [1, 1, 2, 2, 3, 4, 5],
    "num1": [10, 20, 30, 40, 50, 60, 70],
    "num2": [15, 26, 34, 46, 54, 66, 75]
}
df = pd.DataFrame(data)

# Group by "id" and apply different aggregations to num1 and num2
result = df.groupby('id').agg(
    sum_num1=('num1', 'sum'),
    avg_num1=('num1', 'mean'),
    max_num2=('num2', 'max'),
    min_num2=('num2', 'min'),
    count=('id', 'count')
).reset_index()

print(result)
