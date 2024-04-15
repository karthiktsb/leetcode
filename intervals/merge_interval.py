def merge(intervals: list[list[int]]) -> list[list[int]]:
    res = []
    intervals.sort(key=lambda x: x[0])

    def merge(a: list[int], b: list[int]):
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

    if intervals:
        res.append(intervals[0])

    for i in intervals:
        current = merge(i, intervals[-1])
        res.pop()
        res.extend(current)

    return res


if __name__ == '__main__':
    print(merge([[2, 8], [10, 27], [25, 39]]))
    print(merge([[1, 3], [6, 9], [2, 5]]))
    print(merge([]))
