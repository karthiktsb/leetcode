import sys


def largest_subarray_sum(nums: list[int]):
    result = 0
    max_sum = sys.maxsize * -1

    for n in nums:
        result += n
        max_sum = max(max_sum, result)

        if result < 0:
            result = 0

    return max_sum


if __name__ == "__main__":
    print(largest_subarray_sum([-4, 2, -5, 1, 2, 3, 6, -5, 1]))