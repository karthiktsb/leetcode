import numpy as np
import pandas as pd

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

print(df)
grouped = df.groupby("name")

max_sal = grouped["sal"].max()

print(type(max_sal))
print(max_sal.reset_index())
print(type(int(df["sal"].max())))
print(df["sal"])
print(df.describe())
print(type(grouped))



def get_n(group: pd.DataFrame):
    print(type(group))
    group = group.sort_values(by="sal", ascending=False).reset_index()
    if len(group) >= 3:
        return group.iloc[2]
    else:
        group = group.iloc[0]
        group["sal"] = np.NAN
        return group

res = grouped.apply(get_n).reset_index(drop=True)
print(res[["name", "sal"]].to_string(index=False))
print(res[res["sal"] > 100][["name", "sal"]])
print(type(res))

def lag(group: pd.DataFrame):
    group = group.sort_values(by="sal").reset_index()
    group["lag"] = group["sal"].shift().fillna(0)
    group["sum"] = group["sal"].cumsum()
    group["avg"] = group["sum"] / (group.index + 1)
    group["max"] = group["sal"].cummax()
    group["min"] = group["sal"].cummin()
    return group

res1 = grouped.apply(lag).reset_index(drop=True)

print(res1[["name", "sal", "lag", "sum", "avg", "max", "min"]])



# Create a sample DataFrame
data1 = {'fielda': ['A', 'A', 'A', 'B', 'B', 'B'],
        'field1': [10, 5, 15, 7, 20, 3]}
df1 = pd.DataFrame(data1)
df2 = df1
# Sort the DataFrame by 'fielda' and 'field1' to ensure the desired order
df1 = df1.sort_values(by=['fielda', 'field1'])

# Calculate the first and last values within each partition defined by 'fielda'
df1['first_value'] = df1.groupby('fielda')['field1'].transform('first')
df1['last_value'] = df1.groupby('fielda')['field1'].transform('last')
df1['lag_field1'] = df1.groupby('fielda')['field1'].transform(lambda x: x.shift(1)).fillna(0)
df1['lead_field1'] = df1.groupby('fielda')['field1'].transform(lambda x: x.shift(-1)).fillna(0)
df1['cumsum_field1'] = df1.groupby('fielda')['field1'].cumsum()
df1['cummax_field1'] = df1.groupby('fielda')['field1'].cummax()
df1['cummin_field1'] = df1.groupby('fielda')['field1'].cummin()
df1['cummin_avg'] = df1.groupby('fielda')['field1'].cumsum()  / (df1.groupby('fielda')['field1'].cumcount() + 1)

print(df1)

df2 = df2.sort_values(by="field1", ascending=False)
df2["cum_max"] = df2["field1"].cummax()
df2["lead_minus"] = df2["field1"] - df2["field1"].shift(-2).fillna(0)

print(df2)


# Sample DataFrame
data3 = {'Group': ['A', 'A', 'B', 'B', 'A', 'B'],
        'Value': [1, 2, 3, 4, 5, 6]}
df3 = pd.DataFrame(data3)

# Define a custom aggregation function to collect values in a list
def collect_list(series):
    return list(series)

# Group by the 'Group' column and aggregate using the custom function
result = df3.groupby('Group')['Value'].agg(lambda x: list(set(x))).reset_index()

print(result)