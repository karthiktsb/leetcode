def jump(nums: list[int]) -> int:
    result = 0
    l, r = 0, 0

    while l < len(nums) - 2:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        result += 1

    return result


if __name__ == '__main__':
    print(jump([2, 3, 1, 1, 4]))
    print(jump([2, 3, 0, 1, 4]))
