class MyMap:
    def __init__(self):
        self.listed = [[] for _ in range(100)]

    def hash_code(self, key):
        return hash(key) % 100

    def __setitem__(self, key, value):
        index = self.hash_code(key)
        for elem in self.listed[index]:
            if elem[0] == key:
                self.listed[index].remove(elem)
        self.listed[index].append((key, value))
        return

    def __getitem__(self, key):
        index = self.hash_code(key)
        for elem in self.listed[index]:
            if elem[0] == key:
                return elem[1]

        return None

    def add(self, key, value):
        self.__setitem__(key, value)

    def get(self, key, default):
        res = self.__getitem__(key)
        return res if res else default


if __name__ == '__main__':
    map1 = MyMap()

    map1.add(1, 'one')
    map1.add(2, 'two')

    print(map1.get(1, ""))
    print(map1.get(2, ""))
    print(map1.get(3, "Three"))
    print(map1[1])
    print(map1[3])

    map1[4] = "Four"
    map1[2] = "Two"
    map1.add(1,"One")

    print(map1[1])
    print(map1[2])
    print(map1[3])
    print(map1[4])
