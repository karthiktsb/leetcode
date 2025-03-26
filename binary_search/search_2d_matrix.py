def search(matrix: list[list[int]], target: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    l = 0
    r = (m * n) - 1

    while l <= r:
        mid = l + (r - l) // 2
        mid_value = matrix[mid // n][mid % n]

        if target == mid_value:
            return True
        else:
            if target > mid_value:
                l = mid + 1
            else:
                r = mid - 1

    return False


if __name__ == '__main__':
    print(search([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 7))
    print(search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 9))

