def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1


    while (left <= right):
        mid = int(left + (right - left) / 2)

        if nums[mid] == target:
            return mid
        else:
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == '__main__':
    print(binary_search([-1,0,3,5,6,7,8,9,12], 12))
    print(binary_search([-1, 0, 3, 5, 6, 7, 8, 9, 12], -1))
    print(binary_search([-1, 0, 3, 5, 6, 7, 8, 9, 12], 55))
    print(binary_search([-1, 0, 3, 5, 6, 7, 8, 9, 12], 6))