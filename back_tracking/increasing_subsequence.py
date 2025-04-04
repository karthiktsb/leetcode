def length_of_lis(nums: list[int]) -> int:
    res = 0

    def dfs(last_val:int, count: int, index: int):
        nonlocal res
        if index >= len(nums):
            if count > res:
                res = count
            return

        if last_val < nums[index]:
            dfs(nums[index], count + 1, index + 1)

        dfs(last_val, count, index + 1)


    dfs(float("inf") * -1, 0, 0)
    return res


if __name__ == '__main__':
    print(length_of_lis([-1,0,1,2,3,4,5,6,1,2,3]))
    print(length_of_lis([9,1,4,2,3,3,7]))




