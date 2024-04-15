class Solution:
    def generate_parenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(path: str, open_count: int, close_count: int):
            if len(path) == n * 2:
                res.append(path)
                return

            if open_count < n:
                dfs(path + "(", open_count + 1, close_count)

            if close_count < open_count:
                dfs(path + ")", open_count, close_count + 1)


        dfs("", 0, 0)

        return res


if __name__ == '__main__':
    sol = Solution()

    print(sol.generate_parenthesis(5))
    print(sol.generate_parenthesis(3))
