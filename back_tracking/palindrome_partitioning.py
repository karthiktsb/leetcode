def partition(s: str) -> list[list[str]]:
    res = []

    def dfs(path: list[str], index: int):
        if index >= len(s):
            res.append(path.copy())
            return

        for i in range(index + 1, len(s) + 1, 1):
            part = s[index:i]
            if part == part[::-1]:
                path.append(part)
                dfs(path, i)
                path.pop()

    dfs([], 0)

    return res

if __name__ == '__main__':
    print(partition("aab"))

