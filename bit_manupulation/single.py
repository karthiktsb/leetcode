def singleNumber(nums: list[int]) -> int:
    res = 0
    for n in nums:
        res = res ^ n
    return res


if __name__ == '__main__':
    print(singleNumber([1, 2, 2]))
    print(singleNumber([1, 2, 2, 4, 4]))

    print(bin(8))
    print(bin(7))
    print(bin(15))
    print(bin(-8))
    print(8 & 7)
    print(8 | 7)
    print(~7)