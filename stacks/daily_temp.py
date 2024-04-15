def daily_temp(temps: list[int]) -> list[int]:
    res = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)

    return res


if __name__ == '__main__':
    print(daily_temp([73, 74, 75, 71, 69, 72, 76, 73]))
    print(daily_temp([30, 40, 50, 60]))
    print(daily_temp([30, 20, 10, 0]))
