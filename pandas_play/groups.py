import pandas as pd
import numpy as np

if __name__ == '__main__':
    l1 = [
        (1, "alice bale", 100),
        (2, "bea kale", 200),
        (3, "gel mus", 300),
        (4, "man mun", 400),
        (5, "grace", 500),
        (1, "alice bale", 2100),
        (2, "bea kale", 2200),
        (3, "gel mus", 3030),
        (4, "man mun", 4020),
        (5, "grace", 5040),
        (5, "grace", 10040)
    ]

    columns = ["id", "name", "sal"]

    df = pd.DataFrame(l1, columns=columns)

    grouped = df.groupby("id")

    #print(grouped["sal"].value_counts())
    #print(grouped["sal"].agg(["mean", "median", "sum", "count","max", "min"]))
    #print(grouped["sal"].nth(0))


    def get_second_highest_salary(group):
        if len(group) >= 2:
            return group.iloc[len(group) - 2]
        else:
            row = group.iloc[0]
            row["sal"] = np.nan
            return row


    result = df.groupby('id').apply(get_second_highest_salary).reset_index(drop=True)


    # Display the result
    print(result[["id", "sal"]])

    unique_salaries = sorted(df['sal'].unique(), reverse=True)

    print(unique_salaries)

    data1 = {'month': ['01', '02', '03', '05', '04'],
            'sal': [5000, 6000, 7500, 6000, 5500]}

    df1 = pd.DataFrame(data1)

    df1 = df1.sort_values('month')

    df1["cumulative_sum"] = df1["sal"].cumsum()
    df1["cumulative_prod"] = df1["sal"].cumprod()

    print(df1)

    df1["rank"] = df1["sal"].rank(method="dense", ascending=False)
    df1 = df1.sort_values("rank").reset_index()
    df1["row_num"] = df1.index + 1
    df1["prev"] = df1["sal"].shift()
    df1["next"] = df1["sal"].shift(-1)
    print(df1)


    print("~~~~~~~~~~~~~~~~~")

    def map_groups(grp):
        grp["rank"] = grp["sal"].rank(method="dense", ascending=False)
        grp = grp[grp["rank"] == 1]
        return grp

    grouped_rank = grouped.apply(map_groups).reset_index(drop=True)

    temp = pd.DataFrame(df["id"].drop_duplicates())

    merged = pd.merge(temp, grouped_rank, on="id", how="left", suffixes=("_left", "_right"))

    print(merged[["id", "sal"]])

    print(df.groupby("name")["sal"].median())

    def top_3_salaries(group):
        return group.nlargest(3, 'sal')

    # Apply the function to the DataFrame and reset the index
    result = df.groupby('name').apply(top_3_salaries).reset_index(drop=True)

    # Display the result
    print(result)


    # Apply the function to the DataFrame and reset the index
    result = df.groupby('name').nth(1)

    # Display the result
    print(result)

    def get_prev_sal(grp):
        grp["prev"] = grp["sal"].shift()
        return grp

    grp_prv = grouped.apply(get_prev_sal).reset_index(drop=True)

    print(grp_prv.fillna(0))