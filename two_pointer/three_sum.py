def three_sum(nums, target):
    result = []
    nums_sorted = sorted(nums)

    for i in range(len(nums) - 2):
        if i == 0 or nums_sorted[i] != nums_sorted[i - 1]:
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]

                if sum == target:
                    result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])

                    while nums_sorted[left] == nums_sorted[left + 1]:
                        left += 1

                    while nums_sorted[right] == nums_sorted[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                else:
                    if sum < target:
                        left += 1
                    else:
                        right -= 1

    return result


if __name__ == '__main__':
    print(three_sum([-1,0,1,2,-1,-4], 0))
    print(three_sum([1,-1,-1,0], 0))
