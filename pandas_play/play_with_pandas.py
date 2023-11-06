import pandas as pd

if __name__ == "__main__":
    l1 = [
        (1, "alice bale", 100),
        (2, "bea kale", 200),
        (3, "gel mus", 300),
        (4, "man mun", 400),
        (5, "grace", 500)
    ]

    columns = ["id", "name", "sal"]

    df = pd.DataFrame(l1, columns=columns)

    print(df.head(2))

    print(df[["id", "sal"]].tail(1))

    print(df.columns.tolist())

    print("---FILTER-----")

    print(df[(df["id"] > 2) & (df["name"].str.contains("a")) & (df["sal"] == 500)].set_index("id"))

    print("---LOC-----")

    print(df.loc[1:3:2, "name"])
    print(df.loc[~(df["name"].str.contains("a")) & (df["sal"] > 200), ["name", "sal"]])

    data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 22, 34, 56, 43]}

    df1 = pd.DataFrame(data, index=data["Name"])

    print(df1)

    print(df.iloc[0, 1])

    print("---------update---------")
    df["name_len"] = df["name"].apply(len)
    df["high_sal"] = df["sal"] >= 300
    print(df)

    df["sal"] = df["sal"].replace({200: 201, 300: 351})
    df["name"] = df["name"].apply(lambda x: '"' + x + '"')
    print(df)


    def func(x: int) -> int:
        if x % 2 == 0:
            return x * 2
        else:
            return x + 5


    def split_name(s):
        l = s.split(" ")
        if len(l) == 2:
            return pd.Series([l[0], l[1]])
        else:
            return pd.Series([l[0], l[0]])


    df["new_col"] = df["sal"].apply(func)
    print(df)
    cols = df.columns.tolist()
    df.set_index(df["id"], inplace=True)
    df = df[cols[::-1]]
    df[["first", "last"]] = df["name"].apply(split_name)
    print("============")
    df = df.sort_values("name", ascending=False)
    df = df.drop(columns="sal")
    print(df)
    frames = [df, df]
    res = pd.concat(frames)
    print("---------------")
    print(df[df["new_col"] > 300]["new_col"].count())
    print(df.groupby("high_sal")["high_sal"].count())




