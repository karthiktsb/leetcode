def coin_change(amount: int, coins: list[int]) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        i = 0
        while i < len(coins) and a - coins[i] >= 0:
            dp[a] = min(dp[a], 1 + dp[a - coins[i]])
            i += 1
        print(dp)

    if dp[amount] <= amount:
        return dp[amount]
    else:
        return -1


if __name__ == '__main__':
    print(coin_change(14, [1, 5, 9]))
    print(coin_change(11, [1, 5, 9]))
    print(coin_change(3, [2]))
