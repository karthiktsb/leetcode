class MyLazyRange:
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start if start else 0
        self.end = end
        self.step = step
        self.curr= self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr > self.end:
            raise StopIteration

        current = self.curr
        self.curr += self.step
        return current


if __name__ == "__main__":
    lazy_range = MyLazyRange(1, 10)

    #for i in lazy_range:
    #    print(i)
    try:
        n = next(lazy_range)
        while n:
            print(n)
            n = next(lazy_range)
    except StopIteration:
        pass

