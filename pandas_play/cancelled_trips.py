import numpy
import pandas as pd
from datetime import datetime
from datetime import timedelta


def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    unbanned_users = users[users["banned"] == "No"]

    clients = trips.merge(unbanned_users[unbanned_users["role"] == "client"], left_on="client_id", right_on="users_id",
                          how="inner", )

    clients = clients[["id", "status", "request_at", "driver_id"]]
    clients_and_drivers = clients.merge(unbanned_users[unbanned_users["role"] == "driver"], left_on="driver_id",
                                        right_on="users_id", how="inner", suffixes=("_left", "_right"))
    clients_and_drivers = clients_and_drivers[["id", "status", "request_at"]]

    all = clients_and_drivers.groupby("request_at").count().reset_index()
    cancelled = clients_and_drivers[clients_and_drivers["status"] != "completed"].groupby(
        "request_at").count().reset_index()

    res = all[["request_at", "id"]].merge(cancelled[["request_at", "id"]], on="request_at", how="left")

    res["id_y"] = res["id_y"].fillna(res["id_x"])
    res["Cancellation Rate"] = (res["id_y"] / res["id_x"]).round(2)

    print(res[["request_at", "Cancellation Rate"]].rename(columns={"request_at": "Day"}))


def deal_with_dates(trips_df):
    trips_df["request_at"] = pd.to_datetime(trips_df["request_at"])

    trips_df['datetime_field1'] = trips_df['request_at'] + timedelta(days=3000)

    trips_df['days'] = (trips_df['datetime_field1'] - trips_df["request_at"]).dt.days
    # trips_df['hours'] = (trips_df['datetime_field1'] - trips_df["request_at"]).dt.total_seconds() / 3600
    # trips_df['months'] = trips_df['datetime_field1'].dt.month - trips_df["request_at"].dt.month
    trips_df['year'] = trips_df['datetime_field1'].dt.year - trips_df["request_at"].dt.year
    trips_df['start_of_month'] = trips_df['request_at'].dt.to_period('M').dt.to_timestamp()

    print(trips_df)


trips = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "client_id": [1, 2, 3, 4, 1, 2, 3, 2, 3, 4],
    "driver_id": [10, 11, 12, 13, 10, 11, 12, 12, 10, 13],
    "city_id": [1, 1, 6, 6, 1, 6, 6, 12, 12, 12],
    "status": ["completed", "cancelled_by_driver", "completed", "cancelled_by_client", "completed", "completed",
               "completed", "completed", "completed", "cancelled_by_driver"],
    "request_at": ["2013-10-01", "2013-10-01", "2013-10-01", "2013-10-01", "2013-10-02", "2013-10-02", "2013-10-02",
                   "2013-10-03", "2013-10-03", "2013-10-03"]
}

users = {
    "users_id": [1, 2, 3, 4, 10, 11, 12, 13],
    "banned": ["No", "Yes", "No", "No", "No", "No", "No", "No"],
    "role": ["client", "client", "client", "client", "driver", "driver", "driver", "driver"]
}

trips_df = pd.DataFrame(trips)
users_df = pd.DataFrame(users)

trips_and_users(trips_df, users_df)

deal_with_dates(trips_df)
