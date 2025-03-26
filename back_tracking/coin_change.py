import sys


def least_coins(coins: list[int], target: int) -> int:
    res = target + 1

    def dfs(index: int, total: int, num_coins: int):
        nonlocal res
        if index < len(coins) and total <= target:
            if total == target and num_coins < res:
                res = num_coins
                return
            else:
                dfs(index, total + coins[index], num_coins + 1)
                dfs(index + 1, total, num_coins)

    dfs(0, 0, 0)
    return res


if __name__ == '__main__':
    print(least_coins([1, 2, 5], 11))
    print(least_coins([3, 7, 405, 436], 839))
