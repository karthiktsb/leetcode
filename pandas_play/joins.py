import pandas as pd

if __name__ == "__main__":
    data1 = {
        "key1": [1,2,3,4,5,6],
        "values1": ["a", "b", "c", "d", "e", "f"]
    }

    data2 = {
        "key2": [1, 2, 3, 4, 5, 7],
        "values2": ["a", "b", "c", "d", "e", "g"]
    }

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    #df3 = pd.merge(df1, df2, left_on="key1", right_on="key2", how="outer")

    df3 = df1.merge(df2, left_on="key1", right_on="key2", how="outer")
    print(df3)

    data3 = {
        "key": [1, 2, 3, 4, 5, 6],
        "values": ["a", "b", "c", "d", "e", "f"]
    }

    data4 = {
        "key": [1, 2, 3, 4, 5, 7],
        "values": ["a", "b", "c", "d", "e", "g"]
    }

    df4 = pd.DataFrame(data3)
    df5 = pd.DataFrame(data4)

    df6 = pd.concat([df4, df5]).reset_index(drop=True).drop_duplicates()

    print(df6)