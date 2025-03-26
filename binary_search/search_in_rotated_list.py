def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2

        if target == nums[m]:
            return m
        else:
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

    return -1


if __name__ == '__main__':
    print(search([3, 4, 5, 6, 7, 8, 0, 1, 2], 5))
    print(search([5, 6, 7, 8, 1, 2, 3, 4], 19))
    print(search([5, 6, 7, 8, 1, 2, 3, 4], 4))
    print(search([5, 6, 7, 8, 1, 2, 3, 4], 5))
