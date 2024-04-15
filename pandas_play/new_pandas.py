import pandas as pd

data = {
    "f1": [1, 2, 3, 4, 5, 6, 6, 6],
    "f2": ["a", "b", "c", "d", "e", "f", "G", "h"],
    "f3": [345, 544, 2323, 223, 232, 24334, 4764, 3867]
}

df = pd.DataFrame(data)

print(df)
print(df.groupby("f1")["f2"].agg(lambda x: list(x)).reset_index())
print(df.groupby("f1")["f3"].mean().reset_index())
print(df.groupby("f1")["f3"].median().reset_index())