def power(x: int, n: int):
    res = 1
    for i in range(n):
        res *= x

    return res


if __name__ == "__main__":
    print(power(2,5))