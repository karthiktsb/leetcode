def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        summed = nums[left] + nums[right]

        if summed == target:
            return [left, right]
        else:
            if summed <  target:
                left += 1
            else:
                right -= 1

    return []


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([2, 7, 11, 15], 26))
    print(two_sum([2, 7, 11, 15], 29))
