import pandas as pd


def dept_sal(emp, dept):
    emp_df = pd.DataFrame(emp)
    dept_df = pd.DataFrame(dept)

    joined_df = emp_df.merge(dept_df, left_on="departmentId", right_on="id", suffixes=("_left", "_right"))

    joined_df["rank"] = joined_df.groupby("departmentId")["salary"].rank(method="dense", ascending=False).astype(int)

    joined_df = joined_df[joined_df["rank"] <= 3]

    joined_df = joined_df.rename(columns={"name_right": "Department", "name_left": "Employee"})

    joined_df = joined_df.sort_values(by=["Department", "salary"], ascending=[True, False])

    print(joined_df[["Department", "Employee", "salary"]])


emp = {
    "id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["Joe", "Henry", "Sam", "Max", "Janet", "Randy", "Will"],
    "salary": [85000, 80000, 60000, 90000, 69000, 85000, 70000],
    "departmentId": [1, 2, 2, 1, 1, 1, 1, ]
}

dept = {
    "id": [1, 2],
    "name": ["IT", "Sales"]
}

dept_sal(emp, dept)
