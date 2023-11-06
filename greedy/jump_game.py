def can_jump(nums: list[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0


if __name__ == '__main__':
    print(can_jump([2, 3, 1, 1, 4]))
    print(can_jump([3, 2, 1, 0, 4]))
