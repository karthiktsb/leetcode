import sys


def max_sub_array(nums: list[int]) -> int:
    res = nums[0]
    cur_min, cur_max = 1, 1

    for n in nums:
        tmp_max = cur_max * n
        tmp_min = cur_min * n
        cur_max = max(tmp_max, tmp_min, n)
        cur_min = min(tmp_min, tmp_max, n)
        res = max(res, cur_max)

    return res


def max_sub_array_random(nums: list[int]):
    res = [[sys.maxsize * -1]]
    max_prod = sys.maxsize * -1

    def dfs(path: list[int], prod: int, index: int):
        nonlocal max_prod
        if prod > max_prod:
            res.pop()
            res.append(path.copy())
            max_prod = prod

        if index < len(nums):
            path.append(nums[index])
            dfs(path, prod * nums[index], index + 1)
            path.pop()
            dfs(path, prod, index + 1)

    dfs([], 1, 0)

    return res[0]


if __name__ == '__main__':
    print(max_sub_array([1, 2, 3, -4, -5]))
    print(max_sub_array([1, 2, 3, -4, 5]))
    print(max_sub_array_random([1, 2, 3, -4, -5, -10]))
    print(max_sub_array_random([-10, 10, -10]))