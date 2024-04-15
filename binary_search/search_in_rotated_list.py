def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        else:
            if nums[mid] > nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
    return -1


if __name__ == '__main__':
    print(search([3, 4, 5, 6, 7, 8, 0, 1, 2], 5))
    print(search([5, 6, 7, 8, 1, 2, 3, 4], 19))
    print(search([5, 6, 7, 8, 1, 2, 3, 4], 4))
    print(search([5, 6, 7, 8, 1, 2, 3, 4], 5))
