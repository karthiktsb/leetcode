def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left, right]
        else:
            if sum > target:
                right -= 1
            else:
                left += 1

    return []


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([2, 7, 11, 15], 26))
    print(two_sum([2, 7, 11, 15], 29))
