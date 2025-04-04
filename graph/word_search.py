class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def dfs(r: int, c: int, i: int):
            if i == len(word):
                return True

            if (r not in range(ROWS) or
                    c not in range(COLS) or
                    word[i] != board[r][c] or
                    (r, c) in seen):
                return False

            seen.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            seen.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

