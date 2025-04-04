import os

import pandas as pd

def main():
    df = pd.read_csv("../pandas_play/student.csv")
    df1 = df.sort_values(by=["year", "gender", "mark"], ascending=[True, True, False])
    grouped_df = df.groupby(["gender"])

    print(type(grouped_df))

    # Group by a field and get the counts and retain the grouped field (reset_index()) does that.. If reset_index is not used then Year becomes the index
    print(grouped_df.size().to_frame("Count").sort_values("Count", ascending=False).reset_index().head(10))
    print(grouped_df.size().reset_index(name="Count").sort_values("Count").head(10))

    # Get a aggregate of a column with the index reset
    print(grouped_df["mark"].mean().to_frame("avg_marks").sort_values("avg_marks", ascending=False).reset_index().head(10))

    # Multiple aggregation at the same time without resetting index so that gender is the index
    aggragates = grouped_df.agg(
        Count=("mark", "count"),
        Sum=("mark", "sum"),
        Avg=("mark", "mean")
    ).sort_values("Sum", ascending=False)

    # Get the Index where the value is male and get all aggregate values
    print(aggragates[aggragates.index == "male"])

    resetted_df = aggragates.reset_index()
    print(resetted_df[resetted_df["gender"] == "female"])

    # General Aggragations without Group By

    print(df.describe())
    print("------------")
    print(df.shape[0]) # Counts for the num of rows
    print("------------")
    print(df.count())  # Counts for the entire dataframe for non na values
    print("------------")
    print(df["mark"].sum())  # Sum of all marks
    print("------------")
    print(df.agg(
        Count=("mark", "count"),
        Sum=("mark", "sum"),
        Avg=("mark", "mean"),
        Max=("mark", "max"),
        Min=("mark", "min")
    ).reset_index())  # Counts for the entire dataframe for non na values

    print(df.size)

    #print last row
    print(df[df.index == len(df) - 1])


    multiple_groups = df.groupby(["year", "gender"])
    print("------------")
    print(multiple_groups["mark"].sum().reset_index(name="total"))

    print(multiple_groups.get_group((1982, "male")))
    print("------------")
    print(multiple_groups["mark"].agg(["mean", "max", "min", "median"]).reset_index())


    ###################
    # Below Section is for Window Functions
    ##################

    print("#######################################")

    # Dense rank over partition by year and gender and order by mark desc abd get the 2nd ranked person
    df["rank"] = df.groupby(["year", "gender"])["mark"].transform("rank", method="dense", ascending=False)
    print(df[df["year"] == 1982].sort_values("gender"))
    print("------------")
    print(df[df["rank"] == 2.0].sort_values(["year","gender"])[["year", "gender", "name", "mark"]])

    # Row number
    df["row_number"] = df.groupby(["year", "gender"])["mark"].transform("rank", method="first", ascending=False)
    df["cumsum"] = df.sort_values(["year", "gender", "mark"]).groupby(["year", "gender"])["mark"].cumsum()
    df["cummin"] = df.groupby(["year", "gender"])["mark"].transform("cummin")
    df["cummean"] = df.groupby(["year", "gender"])["mark"].expanding().mean().reset_index(level=[0, 1], drop=True)

    print("------------")
    print(df.sort_values(["year", "gender"]))



    df1["lag"] = df1.groupby(["year", "gender"])["mark"].shift(1).fillna(-999).astype(int)
    df1["lead"] = df1.groupby(["year", "gender"])["mark"].shift(-1).fillna(-999).astype(int)

    print("------------")
    print(df1)

    #nth largest, n largest and n smallest in a group
    print("------------")
    sdf = pd.DataFrame({
        'group': ['A', 'A', 'A', 'B', 'B', 'B', 'B'],
        'value': [1, 3, 5, 7, 2, 6, 6]
    })

    print(sdf["value"].nlargest(2))
    print(sdf["value"].nsmallest(3))
    print("------------")
    # Second largest
    print(sdf["value"].nlargest(2).iloc[1])

    # Third smallest
    print(sdf["value"].nsmallest(3).iloc[2])
    print("------------")
    #n largest and smallest in a group
    print(sdf.groupby("group")["value"].nlargest(3))
    print(sdf.groupby("group")["value"].nsmallest(2))
    print("------------")
    # nth largest and smallest in a group
    print(sdf.groupby("group")["value"].nlargest(2).groupby("group").nth(1).reset_index(level=1, drop=True))
    print(sdf.groupby("group")["value"].nsmallest(3).groupby("group").nth(2).reset_index(level=1, drop=True))

    # count distinct values
    print(sdf["value"].nunique())

main()



