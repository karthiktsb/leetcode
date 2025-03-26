def numIslands(grid: list[list]) -> int:
    if not grid or not grid[0]:
        return 0

    islands = 0
    row, col = len(grid), len(grid[0])
    visit = set()

    def dfs(r, c):
        if (
            r not in range(row) or
            c not in range(col) or
            grid[r][c] == "0" or
            (r,c) in visit
        ):
            return

        visit.add((r, c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            dfs(r + dr, c + dc)


    for r in range(row):
        for c in range(col):
            if grid[r][c] == "1" and (r, c) not in visit:
                islands += 1
                dfs(r, c)

    return islands


if __name__ == "__main__":
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
    print(numIslands(grid1))

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
    print(numIslands(grid2))
