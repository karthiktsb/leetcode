def factorial(n: int):
    res = 1
    for i in range(1, n + 1):
        res = res * i

    return res


def fact(n: int):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == '__main__':
    print(factorial(5))
    print(factorial(10))
    print(fact(5))