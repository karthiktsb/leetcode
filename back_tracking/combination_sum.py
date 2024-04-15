def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(path: list[int], index: int, summed: int):
        if index >= len(candidates) or summed > target:
            return

        if summed == target:
            res.append(path.copy())
            return

        path.append(candidates[index])
        dfs(path, index, summed + candidates[index])
        path.pop()
        dfs(path, index + 1, summed)


    dfs([], 0 , 0)
    return res


if __name__ == '__main__':
    print(combinationSum([2, 3, 6, 7], 7))
