import pandas as pd


def determine_if_contiguous(df):
    df.sort_values("values", inplace=True)
    min_val = df["values"].min().astype(int)
    df["prev"] = df.shift(1).fillna(min_val - 1).astype(int)
    df["diff"] = df["values"] - df["prev"]
    return True if len(df.groupby("diff")) == 1 else False


def determine_if_contiguous_improved(df):
    df.sort_values("values", inplace=True)
    min_val = df["values"].min()
    df["prev"] = df.shift(1).fillna(min_val - 1).astype(int)
    df["diff"] = df["values"] - df["prev"]
    return True if df["diff"].eq(1).all() else False

def main():
    df = pd.read_csv("student.csv")
    df1 = df
    df2 = df
    grouped_df = df.sort_values(["year", "mark"]).groupby(["year"])
    df = df.sort_values(["mark"])
    print(df)

    #expanding and rolling methods for full aggregates
    df["cumsum"] = df["mark"].expanding().mean()
    df["min"] = df["mark"].expanding().min()
    df["max"] = df["mark"].expanding().max()
    df["mean"] = df["mark"].expanding().mean()
    df["rolling_sum"] = df["mark"].rolling(3).sum()
    df["rolling_min"] = df["mark"].rolling(3).min()
    df["rolling_max"] = df["mark"].rolling(3).max()

    with pd.option_context("display.max_columns", None):
        print(df.head(10))

    df1["run_mean"] = grouped_df["mark"].expanding().mean().reset_index(level=0, drop=True)

    print(df1)
    df1["run_median"] = grouped_df["mark"].expanding().median().reset_index(level=0, drop=True)
    df1["run_sum"] = grouped_df["mark"].cumsum()
    df1["size"] = grouped_df.cumcount() + 1
    df1["roll_sum_by_2"] = grouped_df["mark"].rolling(2).sum().reset_index(level=0, drop=True)
    print(df1.reset_index().sort_values(["year", "mark"])[["year", "mark", "run_mean", "run_median", "run_sum", "size", "roll_sum_by_2"]])

    # Learn about indexes
    df3 = df.sort_values(["year", "mark"]).reset_index(drop=True)
    print(df3)
    df3["running_sum"] = df3.groupby("year")["mark"].cumsum()
    print(df3.sort_values(["year", "mark"])[["year", "mark", "running_sum"]])

    print(df3.groupby("year")["mark"].expanding().sum().reset_index(level=0, drop=True))
    print(df3.groupby(["year", "gender"])["mark"].cumsum())


    print(df.groupby(["year", "gender"])["mark"].sum().reset_index(level=1))

    print("-------------")
    #Pivot after group by
    df4 = df.groupby(["year", "gender"])["mark"].sum().reset_index(name="total_marks")
    pivot_df = df4.pivot(index="year", columns="gender", values="total_marks")
    print(pivot_df)

    # pivot without groupby

    pivot_df1 = df.pivot_table(index="year", columns="gender", values="mark", aggfunc="sum", fill_value=100)
    print(pivot_df1)
    with pd.option_context("display.max_columns", None):
        print(df)

    # Filter after grouping - Having clause
    print(df.groupby(["year", "gender"])["name"].first().reset_index(name="first_person"))
    print(df.groupby(["year", "gender"])["mark"].last().reset_index(name="last_person"))
    df5 = df.groupby(["year", "gender"]).size().reset_index(name="count")
    print(df5[(df5["count"] >= 3) & (df5["gender"] == "male")])
    print(df5[(df5["count"] > 3) | (df5["gender"] == "female")])

    # Check for contiguous numbers
    print(determine_if_contiguous_improved(pd.DataFrame({"values": [1, 2, 3, 4, 5, 6, 7, 8, 9]})))
    print(determine_if_contiguous_improved(pd.DataFrame({"values": [1, 2, 10, 3, 4, 5, 6, 7, 8, 9, -1, 0]})))
    print(determine_if_contiguous_improved(pd.DataFrame({"values": [1, 2, 10, 3, 4, 5, 6, 7, 8, 9, 12]})))


main()