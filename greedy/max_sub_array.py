import sys


def max_sum_array(nums: list[int]) -> int:
    result = 0
    max_sum = sys.maxsize * -1

    for n in nums:
        result += n
        max_sum = max(max_sum, result)
        if result < 0:
            result = 0

    return max_sum


if __name__ == '__main__':
    print(max_sum_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sum_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
