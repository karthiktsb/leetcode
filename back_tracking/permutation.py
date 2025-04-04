def permutate(nums: list[int]):
    res = []

    def dfs(idx: int, path: list[int]):
        if idx == len(nums) - 1:
            res.append(path.copy())
            return

        for i in range(idx, len(path)):
            nums[idx], nums[i] = nums[i], nums[idx]
            dfs(idx + 1, path)
            nums[idx], nums[i] = nums[i], nums[idx]

    dfs(0, nums)
    return res


def permutations_recursive(nums: list[int]):
    if len(nums) <= 0:
        return [[]]

    perms = permutations_recursive(nums[1:])
    res = []

    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, nums[0])
            res.append(p_copy)

    return res


if __name__ == "__main__":
    print(permutate([1,2,3]))
    print(permutate([1, 2]))
    print(permutate([1, 2, 3, 4]))
    print(permutations_recursive([1,2,3]))