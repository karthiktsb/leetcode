def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    prevEnd = intervals[0][1]
    res = 0

    for i in range(1, len(intervals)):
        if prevEnd > intervals[i][0]:
            res += 1
        else:
            prevEnd = intervals[i][1]

    return res


if __name__ == '__main__':
    print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(eraseOverlapIntervals([[1, 2], [2, 3], [4, 6]]))
