import pandas as pd

if __name__ == "__main__":
    import pandas as pd

    df1 = pd.DataFrame({
        "FieldA1": [1, 2, 3, 3],
        "FieldA2": ["X", "Y", "Z", "Z"],
        "Field3": ["foo", "bar", "baz", "beta"]
    })

    # df2 with FieldB1, FieldB2
    df2 = pd.DataFrame({
        "FieldB1": [2, 3, 4, 3],
        "FieldB2": ["Y", "Z", "W", "Z"],
        "Field3": ["alpha", "beta", "gamma", "beta"]
    })

    # Merge - inner join
    df3 = pd.merge(df1, df2, left_on=["FieldA1", "FieldA2"], right_on=["FieldB1", "FieldB2"], how="inner", suffixes=["_df1", "_df2"])
    df4 = pd.merge(df1, df2, left_on=["FieldA1", "FieldA2"], right_on=["FieldB1", "FieldB2"], how="left", suffixes=["_df1", "_df2"])

    print(df3)
    # Drop duplicates it will drop duplicates where all columns match
    print(df3.drop_duplicates())

    print(df4)
    print(df4.drop_duplicates(subset=["FieldA1", "FieldA2"], keep="first"))
    # Drop duplicates and keep last and drop rows with nulls in FieldB1 and drop column FieldB2
    print(df4.drop_duplicates(subset=["FieldA1", "FieldA2"], keep="last").dropna(subset=["FieldB1"]).drop(["FieldB2"], axis=1))

    # Concat - union when done with axis = 0, when axis = 1, then is col addition
    # Unlike sql, the shapes and fields dont have to match
    df5 = pd.concat([df1, df2], axis=0)
    print(df5)

    df6 = (pd.concat([df1, df2], axis=1))
    print(df6)
