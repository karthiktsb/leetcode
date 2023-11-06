def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    prev_end = intervals[0][1]
    result = 0

    for i in intervals[1:]:
        start, end = i[0], i[1]

        if start >= prev_end:
            prev_end = end
        else:
            result += 1
            prev_end = min(end, prev_end)

    return result


if __name__ == '__main__':
    print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(eraseOverlapIntervals([[1, 2], [2, 3], [4, 6]]))
