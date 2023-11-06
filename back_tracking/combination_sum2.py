def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    candidates_sorted = sorted(candidates)

    def dfs(path: list[int], index: int, total: int):
        if index >= len(candidates) or total > target:
            return

        if total == target:
            res.append(path.copy())
            return

        path.append(candidates_sorted[index])
        dfs(path, index + 1, total + candidates_sorted[index])
        next_index = index + 1
        while next_index < len(candidates_sorted) and candidates_sorted[next_index] == candidates_sorted[index]:
            next_index += 1
        path.pop()
        dfs(path, next_index, total)

    dfs([], 0, 0)

    return  res

if __name__ == '__main__':
    print(combinationSum2([10,1,2,7,6,1,5], 8))