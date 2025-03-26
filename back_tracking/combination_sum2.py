def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    scandidates = sorted(candidates)

    def dfs(path: list[int], index: int, summed: int):
        if index >= len(scandidates) or summed > target:
            return

        if summed == target:
            res.append(path.copy())
            return

        path.append(scandidates[index])
        dfs(path, index + 1, summed + scandidates[index])

        next_index = index
        while next_index < len(scandidates) and scandidates[next_index] == scandidates[index]:
            next_index += 1

        path.pop()
        dfs(path, next_index, summed)

    dfs([], 0, 0)
    return res

if __name__ == '__main__':
    print(combinationSum2([10,1,2,7,6,1,5], 8)) #[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]