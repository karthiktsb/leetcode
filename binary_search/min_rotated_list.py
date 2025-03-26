def min_rotated(nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1
    minval = float("inf")

    while l <= r:
        m = l + (r - l) // 2
        minval = min(minval, nums[m])

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m - 1

    return min(minval, nums[l])


if __name__ == '__main__':
    print(min_rotated([3, 4, 5, 6, 7, 8, 0, 1, 2]))
    print(min_rotated([5, 6, 7, 8, 1, 2, 3, 4]))
    print(min_rotated([3, 0, 1]))
