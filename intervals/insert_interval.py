def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    res = []

    def check_intervals(a: list[int], b:list[int]) -> list[list[int]]:
        if a[0] >= b[0]:
            if a[0] <= b[1]:
                return [[b[0], max(a[1], b[1])]]
            else:
                return [b, a]
        else:
            if b[0] <= a[1]:
                return [[a[0], max(a[1], b[1])]]
            else:
                return [a, b]

    res.append(newInterval)

    for i in intervals:
        checked = check_intervals(i, res[-1])
        res.pop()
        res.extend(checked)

    return res


if __name__ == '__main__':
    print(insert([[2, 8], [10, 27]], [25, 39]))
    print(insert([[1, 3], [6, 9]], [4, 7]))
    print(insert([[1, 3], [6, 9]], [4, 5]))
    print(insert([[1,3],[4,6]], [2,5]))
