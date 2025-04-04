class Solution:
    def rob(self, nums: list[int]) -> int:
        result = 0

        def dfs(amount: int, index: int):
            nonlocal result
            if index >= len(nums):
                if amount > result:
                    result = amount
                return

            dfs(amount + nums[index], index + 2)
            dfs(amount, index + 1)

        dfs(0, 0)
        return result


def main():
    fix = Solution()
    print(fix.rob([1,1,3,3]))


main()