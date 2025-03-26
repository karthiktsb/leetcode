def binary_search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        else:
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


if __name__ == '__main__':
    print(binary_search([-1, 0, 3, 5, 6, 7, 8, 9, 12], 12))
    print(binary_search([-1, 0, 3, 5, 6, 7, 8, 9, 12], -1))
    print(binary_search([-1, 0, 3, 5, 6, 7, 8, 9, 12], 55))
    print(binary_search([-1, 0, 3, 5, 6, 7, 8, 9, 12], 6))