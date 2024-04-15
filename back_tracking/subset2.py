class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums_sorted = sorted(nums)

        def dfs(path: list[int], index: int):
            if index >= len(nums):
                res.append(path.copy())
                return

            path.append(nums_sorted[index])
            dfs(path, index + 1)

            next_index = index + 1
            while next_index < len(nums) and nums_sorted[next_index] == nums_sorted[index]:
                next_index += 1

            path.pop()
            dfs(path, next_index)

        dfs([], 0)

        return res


if __name__ == '__main__':
    sol = Solution()

    print(sol.subsetsWithDup([1,2,2]))
    print(sol.subsetsWithDup([0, 0]))
