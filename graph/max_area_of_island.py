def get_max_area(grid: list[list]) -> int:
    max_area = 0
    visit = set()
    row, col = len(grid), len(grid[0])

    def dfs(r, c):
        if (
                r not in range(row)
                or c not in range(col)
                or grid[r][c] == 0
                or (r, c) in visit
        ):
            return 0

        visit.add((r, c))
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1 and (r, c) not in visit:
                max_area = max(dfs(r, c), max_area)

    return max_area


if __name__ == '__main__':
    grid1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(get_max_area(grid1))