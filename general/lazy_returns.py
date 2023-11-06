class FibinocciGen:
    def __init__(self, n):
        self.n = n

    def gen_fibi(self):
        a, b = 0, 1
        current = 0

        while current < self.n:
            yield a

            a,b = b, a + b
            current += 1

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

