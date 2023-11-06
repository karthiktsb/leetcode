def insert_index(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = int(left + (right - left) / 2)

        if nums[mid] < target:
            left += 1
        else:
            right -= 1

    return left


if __name__ == '__main__':
    print(insert_index([1,3,5,7,18], 9))
    print(insert_index([1, 3, 5, 7, 18], 19))
    print(insert_index([1, 3, 5, 7, 18], 0))
    print(insert_index([1, 3, 5, 7, 18], 2))