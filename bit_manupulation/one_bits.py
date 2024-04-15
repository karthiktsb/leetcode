def hammingWeight(n: int) -> int:
    res = 0
    while n:
        n &= n - 1
        res += 1
        print(n)
    return res


if __name__ == '__main__':
    print(bin(10))
    print(hammingWeight(10))
    print(bin(8))
    print(hammingWeight(8))
    print(bin(7))
    print(hammingWeight(7))