class MyMap:
    def __init__(self):
        self.my_map = [[] for _ in range(100)]

    def hash_code(self, key):
        return hash(key) % 100

    def add(self, key, value):
        self.__setitem__(key, value)

    def get(self, key, default):
        index = self.hash_code(key)
        for entry in self.my_map[index]:
            if entry[0] == key:
                return entry[1]
        return default

    def __getitem__(self, item):
        index = self.hash_code(item)
        for elem in self.my_map[index]:
            if elem[0] == item:
                return elem[1]

        return None

    def __setitem__(self, key, value):
        index = self.hash_code(key)
        for elem in self.my_map[index]:
            if elem[0] == key:
                self.my_map[index].remove(elem)

        self.my_map[index].extend([(key,  value)])
        return


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
