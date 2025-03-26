class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        len_nums =  len(nums)

        def dfs(path: list[int], index:int):
            if index >= len_nums:
                res.append(path.copy())
                return

            path.append(nums[index])
            dfs(path, index + 1)
            path.pop()
            dfs(path, index + 1)

        dfs([], 0)
        return res


if __name__ == '__main__':
    sol = Solution()

    print(sol.subsets([1, 2, 3]))
    print(sol.subsets([0]))
