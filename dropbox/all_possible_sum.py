def all_possible_sum(num: int) -> list[int]:
    res = []

    def dfs(path: list[int], total: int, curr: int):
        if total == num:
            res.append(path.copy())
            return

        if total > num or curr > num:
            return

        path.append(curr)
        dfs(path, total + curr, curr)
        path.pop()
        dfs(path, total, curr + 1)

    dfs([], 0, 1)
    return res


if __name__ == "__main__":
    print(all_possible_sum(5))
    print(all_possible_sum(0))
    print(all_possible_sum(1))
    print(all_possible_sum(2))
    print(all_possible_sum(10))

