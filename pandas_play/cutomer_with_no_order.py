import pandas as pd


def customers(cust, orders):
    cust_df = pd.DataFrame(cust)

    orders_df = pd.DataFrame(orders)

    joined = cust_df.merge(orders_df, left_on="id", right_on="customerId", suffixes=("_left", "_right"), how="left")

    joined = joined[joined["customerId"].isna()]

    joined = joined.rename(columns={"name": "Customers"})

    print(joined["Customers"].reset_index(drop=True))


cust = {
    "id": [1, 2, 3, 4],
    "name": ["Joe", "Henry", "Sam", 'Max']
}

orders = {
    "id": [1, 2],
    "customerId": [3, 1]
}

customers(cust, orders)
