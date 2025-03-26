class MyHeap:
    def __init__(self, order):
        self.buffer = []
        if order not in ["asc", "desc"]:
            raise Exception("Order should be ASC or DESC")
        self.order = order

    def enqueue(self, value):
        index = self.insert_index(value)
        self.buffer.insert(index, value)
        return

    def insert_index(self, value):
        if not self.buffer:
            return 0

        l, r = 0 , len(self.buffer) - 1

        while l <= r:
            m = l + (r - l) // 2

            if self.buffer[m] == value:
                return m
            else:
                if value > self.buffer[m]:
                    l = m + 1
                else:
                    r = m - 1

        return l

    def dequeue(self):
        if self.buffer:
            if self.order == "asc":
                return self.buffer.pop(0)
            else:
                return self.buffer.pop()
        else:
            None


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

    pq1 = MyHeap("asc")

    pq1.enqueue(5)
    pq1.enqueue(3)
    pq1.enqueue(1)
    pq1.enqueue(2)

    print(pq1.dequeue())
    print(pq1.dequeue())
    print(pq1.dequeue())
    print(pq1.dequeue())
    print(pq1.dequeue())
