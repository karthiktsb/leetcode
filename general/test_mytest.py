import pandas as pd

from .data_source import DataSource
from pandas.testing import assert_frame_equal
from pyspark.sql import SparkSession

def add(a, b):
    return a + b


def test_addition():
    assert add(1, 3) == 4


def test_myLists():
    l1 = [1, 2, 3, 4, 5]
    l2 = [1, 2, 3, 5, 4]

    assert l1.sort() == l2.sort()

    d1 = {"a": 1, "b": 2}
    d2 = {"b": 2, "a": 1}

    assert d1 == d2


def test_data_source():
    ds1 = DataSource([1, 2, 3, 4])
    ds2 = DataSource([1, 2, 3, 4])

    assert ds1 == ds2


def test_none_list():
    l1 = [None] * 5
    l2 = [None] * 5

    assert l1 == l2


def test_frames():
    data1 = {
        "f1": [1, 2, 3, 4, 5],
        "f2": [6, 7, 8, 9, 0]
    }

    data2 = {
        "f1": [1, 2, 3, 4, 5],
        "f2": [6, 7, 8, 9, 0]
    }

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    assert_frame_equal(df1, df2)


def test_spark_dataframe():
    spark = SparkSession.builder.appName("example").getOrCreate()

    # Create two Spark DataFrames for comparison
    data1 = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    data2 = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

    columns = ["Name", "Age"]

    df1 = spark.createDataFrame(data1, columns)
    df2 = spark.createDataFrame(data2, columns)

    assert df1.collect() == df2.collect()