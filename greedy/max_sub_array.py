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


def max_array_non_contiguous(nums: list[int]):
    res = [[sys.maxsize * -1]]

    def dfs(path: list[int], summed: int, index: int):
        if res and summed > sum(res[0]):
            res.pop()
            res.append(path.copy())

        if index >= len(nums):
            return

        path.append(nums[index])
        dfs(path, summed + nums[index], index + 1)
        path.pop()

        dfs(path, summed, index + 1)

    dfs([], 0, 0)

    return res


if __name__ == '__main__':
    print(max_sum_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sum_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sum_array([-4, -2, -3, -4, -1]))
    print(max_array_non_contiguous([-2, 1, -3, 4, -1, 2, 1, -5, 4, 9]))
