def myPow(x: float, n: int) -> float:
    def helper(x1: float, n1: int):
        if x1 == 0:
            return 0
        if n1 == 0:
            return 1

        res = helper(x1, n1 // 2)
        res = res * res

        return x1 * res if n % 2 == 1 else res

    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res


def main():
    print(myPow(2.0, 5))


main()