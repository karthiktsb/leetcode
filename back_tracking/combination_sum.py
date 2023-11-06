def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(path: list[int], index: int, total: int):
        if index >= len(candidates) or total > target:
            return

        if total == target:
            res.append(path.copy())
            return

        path.append(candidates[index])
        dfs(path, index, total + candidates[index])
        path.pop()
        dfs(path, index + 1, total)

    dfs([], 0, 0)
    return res


if __name__ == '__main__':
    print(combinationSum([2, 3, 6, 7], 7))
