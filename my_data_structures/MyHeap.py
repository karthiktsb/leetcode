class MyHeap:
    def __init__(self, order):
        self.buffer = []
        if order.upper() != "ASC" and order.upper() != "DESC":
            raise Exception("Order has to be asc or desc")
        self.order = order

    def enqueue(self, value):
        index = self.insert_index(value)
        self.buffer.insert(index, value)
        return

    def insert_index(self, value):
        if not self.buffer:
            return 0

        l, r = 0, len(self.buffer) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if self.buffer[mid] == value:
                return mid
            else:
                if value > self.buffer[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return l

    def dequeue(self):
        if self.order == "ASC":
            elem = self.buffer[0]
            self.buffer.pop(0)
            return elem
        else:
            elem = self.buffer[-1]
            self.buffer.pop()
            return elem

    def head(self):
        if self.order == "ASC":
            return self.buffer[0]
        else:
            return self.buffer[-1]

    def length(self):
        return len(self.buffer)


if __name__ =='__main__':
    pq = MyHeap("desc")

    pq.enqueue(5)
    pq.enqueue(1)
    pq.enqueue(3)
    pq.enqueue(2)

    print(pq.head())
    print(pq.dequeue())
    print(pq.head())
    print(pq.dequeue())
    print(pq.head())
