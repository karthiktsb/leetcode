import numpy as np
import itertools

if __name__ == "__main__":
    a = np.array([1, 2, 3, 4, 5, 6])
    ca = np.array([2, 3, 4, 5, 6, 7])

    print(a.itemsize)
    print(a.nbytes)
    print(a.cumsum())
    print(a.cumprod())
    print(np.diff(a))
    print(np.multiply.accumulate(a))
    print(a < 4)
    a *= 2
    print(a)
    print(a.shape)
    print(a.max())
    print(a.mean())
    print(a.mean())
    print(np.any(a > 5))
    print(np.all(a > 0))

    n = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 6, 5]]
    b = np.array(n)
    print(b.shape)

    l = [1, 2, 3, 4, 5, 6, 6]
    m = [1, 2, 3, 4, 5, 6, 6]


    def remove_dups(l1):
        l2 = []

        for i in l1:
            if i not in l2:
                l2.append(i)

        return l2


    print(remove_dups(l))

    for i in itertools.product(l, m):
        print(i)

    for j in itertools.chain.from_iterable(n):
        print(j)

    print("~~~~~~~~~~~")
    k = [6, 5, 4, 3, 2, 1]
    for i in itertools.accumulate(k):
        print(i)

    for i in itertools.permutations(k, 2):
        print(i)
    print("~~~~~~~~~~~")
    for i in itertools.combinations(k, 2):
        print(i)

    # x = (x * 3 for x in l)
    x = (x * 3 for x in range(2, 4))
    try:
        y = next(x)
        while y:
            print(y)
            y = next(x)
    except StopIteration:
        pass
