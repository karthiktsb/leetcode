def three_sum(nums, target):
    res = []
    nums_sort = sorted(nums)

    for i in range(len(nums) - 2):
        if i == 0 or nums_sort[i] != nums_sort[i - 1]:
            left = i + 1
            right = len(nums_sort) - 1

            while left < right:
                summed = nums_sort[i] + nums_sort[left] + nums_sort[right]
                if summed == target:
                    res.append([nums_sort[i], nums_sort[left], nums_sort[right]])

                    while nums_sort[left] == nums_sort[left + 1]:
                        left += 1

                    while nums_sort[right] == nums_sort[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                else:
                    if summed < target:
                        left += 1
                    else:
                        right -= 1

    return res


if __name__ == '__main__':
    print(three_sum([-1,0,1,2,-1,-4], 0))
    print(three_sum([1,-1,-1,16, 1], 18))
    print(three_sum([1, -1, -1, 0],-2))
