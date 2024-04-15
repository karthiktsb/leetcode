def max_sub_array(nums: list[int]) -> int:
    res = nums[0]
    cur_max, cur_min = 1, 1

    for n in nums:
        tmp_max = cur_max * n
        tmp_min = cur_min * n
        cur_max = max(tmp_min, tmp_max, n)
        cur_min = min(tmp_min, tmp_max, n)
        res = max(res, cur_max)

    return res


if __name__ == '__main__':
    print(max_sub_array([1, 2, 3, -4, -5]))
    print(max_sub_array([1, 2, 3, -4, 5]))
