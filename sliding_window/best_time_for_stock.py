def max_profit(prices: list[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for i in prices:
        max_profit = max(max_profit, i - min_price)
        min_price = min(min_price, i)

    return max_profit


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([7, 6, 4, 3, 1]))
    print(max_profit([1, 2, 3, 4, 21, 5, 6, 7, 18]))
