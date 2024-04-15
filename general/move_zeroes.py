def move_zeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)

    return nums


print(move_zeroes([0, 1, 2, 3, 0, 9, 7, 0, 8, 7]))
