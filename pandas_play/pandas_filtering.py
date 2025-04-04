import pandas as pd


def main():
    df = pd.read_csv("../pandas_play/student.csv")
    print(df)
    print("---------")
    print(df[df["name"].str.contains("J")])
    print("---------")
    print(df[df["name"].str.startswith("J")])
    print("---------")
    print(df[df["name"].str.endswith("a")])
    print("---------")
    print(df[df["name"].str[:3] == "Joh"])

    # String Methods -
    # str.contains('[aeiou]', case=False, na=False): Check
    # for substrings or regular expressions within a string.
    # str.startswith(), str.endswith(): Check for prefix or suffix matching.
    # str.match('^[AB]'): Matches a string to a regular expression.
    # str.len(): Filter based on string length.
    # str.isnumeric(), str.isalpha(): Check if the string is purely numeric or alphabetic.
    # str.replace('New', 'Old'): Replace substrings and filter accordingly.
    # str.strip(): Remove leading / trailing whitespaces.

    # Multiple condition filtering

    print("---------")
    print(df[((df["name"].str.startswith("J")) | (df["year"] == 1984)) & (df["gender"] == "male")])

    # Dates

    data = {'date': ['2021-01-01', '2021-05-10', '2022-07-15', '2022-10-20'],
            'value': [10, 20, 30, 40]}
    df1 = pd.DataFrame(data)
    df1["date"] = pd.to_datetime(df1["date"])

    print(df1[df1["date"] > "2021-05-11"])
    print(df1[(df1["date"] >= "2021-05-10") & (df1["date"] <= "2022-07-16")])
    print(df1[df1["date"].dt.year == 2021])
    print(df1[df1["date"].dt.month == 5])
    print(df1[df1["date"].dt.quarter == 1])

    df1["prev_date"] = df1["date"].shift(1)
    df1["diff"] = df1["date"] - df1["prev_date"]
    print(df1)

    data = {'date': ['2025-04-01', '2025-04-02', '2025-04-03', '2025-04-04'],
            'value': [10, 20, 30, 40]}

    df3 = pd.DataFrame(data)
    df3["date"] = pd.to_datetime(df3["date"])

    data_diff = df3["date"].diff().dt.days.dropna()
    print(data_diff)
    print((data_diff == 1).all())

    # Timestamp

    data = {'datetime': ['2025-01-01 08:30:00', '2025-03-01 10:45:00', '2025-01-01 15:00:00'],
            'value': [10, 20, 30]}
    df2 = pd.DataFrame(data)
    df2["datetime"] = pd.to_datetime(df2["datetime"])

    print(df2[df2["datetime"].dt.hour >= 10])

    date_diff = pd.to_datetime('today') - pd.DateOffset(days=90)
    print(df2[df2["datetime"] > date_diff])




main()