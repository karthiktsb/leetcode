def all_possible_sum(num: int) -> list[int]:
    res = []

    def dfs(path: list[int], total: int, index: int):
        if total >= num:
            if total == num:
                res.append(path.copy())
            return

        if index <= num:
            path.append(index)
            dfs(path, total + index, index)
            path.pop()
            dfs(path, total, index + 1)

    dfs([], 0, 1)
    return res


if __name__ == "__main__":
    print(all_possible_sum(5))
    print(all_possible_sum(0))
    print(all_possible_sum(1))
    print(all_possible_sum(2))
    print(all_possible_sum(10))

