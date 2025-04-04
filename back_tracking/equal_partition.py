class Solution:
    def can_partition(self, nums: list[int]) -> bool:
        total = sum(nums)
        result = False
        if total % 2 != 0:
            return False

        def dfs(current_sum: int, index: int):
            nonlocal result

            if result:
                return

            if current_sum >= total / 2:
                if current_sum == total / 2:
                    result = True
                return

            if index < len(nums):
                dfs(current_sum + nums[index], index + 1)
                dfs(current_sum, index + 1)

        dfs(0, 0)
        return result


def main():
    fix = Solution()

    print(fix.can_partition([1, 2, 3, 4]))
    print(fix.can_partition([1, 2, 3, 4, 5]))


main()

