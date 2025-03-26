class FibinocciGen:
    def __init__(self, n):
        self.n = n

    def gen_fibi(self):
        a, b = 0, 1
        curr = 0

        if curr == 0:
            yield 0
            curr += 1

        if curr == 1:
            yield 1
            curr += 1

        while curr < self.n:
            yield a + b

            temp = a + b
            a = b
            b = temp
            curr += 1

    def my_generator(m: list[int]):
        for i in m:
            yield i * 2


if __name__ == "__main__":
    fib = FibinocciGen(10)

    gen = FibinocciGen.my_generator(range(10))

    for i in gen:
        print(i)

    for i in fib.gen_fibi():
        print(i)

