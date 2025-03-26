def missing_one_item(nums: list[int], n: int):

    actual = sum(nums)
    expected = n * (n + 1) // 2

    return expected - actual


def main():
    print(missing_one_item([1,3,4,5,6], 6))


main()