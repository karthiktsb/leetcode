class MyIterable:
    def __init__(self):
        self.buffer = []

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.buffer):
            item = self.buffer[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.buffer[item]

    def __setitem__(self, key, value):
        self.buffer[key] = value

    def append(self, value):
        self.buffer.append(value)

    def insert(self, key, value):
        self.buffer.insert(key, value)


if __name__ == '__main__':
    my_list = MyIterable()

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.insert(0, 5)

    my_list[2] = 8

    for i in my_list:
        print(i)
