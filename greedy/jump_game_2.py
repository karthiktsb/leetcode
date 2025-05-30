def jump(nums: list[int]) -> int:
    res = 0
    l, r = 0, 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        res += 1

    return res


if __name__ == '__main__':
    print(jump([2, 3, 1, 1, 4]))
    print(jump([2, 3, 0, 1, 4]))
    print(jump([1, 1, 1, 1, 4]))
    print(jump([5, 1, 1, 1, 4]))
