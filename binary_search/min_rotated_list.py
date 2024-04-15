def min_rotated(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    min_value = float("inf")

    while left <= right:
        mid = left + (right - left) // 2
        min_value = min(min_value, nums[mid])

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1

    return min(min_value, nums[left])


if __name__ == '__main__':
    print(min_rotated([3, 4, 5, 6, 7, 8, 0, 1, 2]))
    print(min_rotated([5, 6, 7, 8, 1, 2, 3, 4]))
