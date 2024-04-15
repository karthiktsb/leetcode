class DataSource:
    def __init__(self, arr):
        self.arr = arr

    def __eq__(self, other):
        if isinstance(other, DataSource):
            return self.arr == other.arr
        return False

    def __contains__(self, n):
        if n in self.arr:
            return True
        return False

    def __len__(self):
        return len(self.arr)

    def __str__(self):
        temp = [str(i) for i in self.arr]
        return "|".join(temp)

    def __getitem__(self, item):
        if item >= len(self.arr):
            raise Exception("Array out of bound")
        else:
            return self.arr[item]

    def __setitem__(self, key, value):
        if key >= len(self.arr):
            raise Exception("Array out of bound")
        else:
            self.arr[key] = value
            return

    def map(self, func):
        temp = [func(item) for item in self.arr]
        return DataSource(temp)

    def filter(self, func):
        temp = [item for item in self.arr if func(item)]
        return DataSource(temp)

    def collect(self):
        return self.arr


ds = DataSource([1, 2, 3, 4])
print(ds.collect())

ds1 = ds.map(lambda x: x * x)
print(ds1.collect())

ds2 = ds.filter(lambda x: x % 2 == 0)
print(ds2.collect())

ds3 = ds.map(lambda x: x * x).filter(lambda x: x % 2 == 0)
print(ds3.collect())

l = [1, 2, 3, 6, 7, 8]

for i in l:
    if i in ds:
        print(i)

print(len(ds))
print(str(ds))
print(ds[2])
ds[2] = 20
print(ds[2])
print("END of DataSourceLazy class test")
print("############" * 10)

k = [1, 3, 5, 6]
print('~~~~~~~')
for i in k:
    print(i)
    if i in ds:
        print(i)
print('~~~~~~~')
class LazyDataSource:
    def __init__(self, arr):
        self.arr = arr

    def map(self, func):
        temp = (func(item) for item in self.arr)
        return LazyDataSource(temp)

    def filter(self, func):
        temp = (item for item in self.arr if func(item))
        return LazyDataSource(temp)

    def collect(self):
        if isinstance(self.arr, list):
            return self.arr
        else:
            return list(self.arr)


dsl = LazyDataSource([1, 2, 3, 4])
print(dsl.collect())

dsl1 = dsl.map(lambda x: x * x)
print(dsl1.collect())

dsl2 = dsl.filter(lambda x: x % 2 == 0)
print(dsl2.collect())

dsl3 = dsl.map(lambda x: x * x).filter(lambda x: x % 2 == 0)
print(dsl3.collect())

print("END of LazyDataSourceLazy class test")
print("############" * 10)


def return_uter(l):
    for i in l:
        yield i * i


print(return_uter([12, 3, 2, 21, 6]))
