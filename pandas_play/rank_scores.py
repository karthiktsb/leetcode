import pandas as pd

def rank_scores(data):
    df = pd.DataFrame(data)


    df["rank"] = df["score"].rank(method="dense", ascending=False).astype(int)

    df = df.sort_values(by="rank").reset_index()

    print(df[["score", "rank"]])


data = {
    "id": [1,2,3,4,5,6],
    "score": [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}

rank_scores(data)