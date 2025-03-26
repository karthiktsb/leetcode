class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        snums = sorted(nums)
        len_nums = len(snums)

        def dfs(path: list[int], index:int):
            if index >= len_nums:
                res.append(path.copy())
                return

            path.append(snums[index])
            dfs(path, index + 1)

            next_index = index
            while next_index < len(snums) and snums[next_index] == snums[index]:
                next_index += 1

            path.pop()
            dfs(path, next_index)

        dfs([], 0)
        return res


if __name__ == '__main__':
    sol = Solution()

    print(sol.subsetsWithDup([1,2,2]))
    print(sol.subsetsWithDup([0, 0]))
