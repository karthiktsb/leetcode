def find_insert_index(in_list: list[int], value: int) -> int:
    if not in_list:
        return 0

    l, r = 0, len(in_list) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if in_list[mid] == value:
            return mid
        else:
            if value > in_list[mid]:
                l = mid + 1
            else:
                r = mid - 1

    return l

def kth_largest(k: int, in_list: list[int]) -> int:
    count = 0
    res = []

    for i in in_list:
        if count > k - 1:
            if i > res[-1]:
                index = find_insert_index(res, i)
                res.pop()
                res.insert(index, i)
        else:
            index = find_insert_index(res, i)
            res.insert(index, i)

        count += 1

    return res[-1]


def kth_largest_new(k: int, in_list: list[int]) -> int:
    result = []

    for i in range(len(in_list)):
        index = find_insert_index(result, in_list[i])
        result.insert(index, in_list[i])
        if i > k - 1:
            result.pop(0)

    return result[0]


if __name__ == '__main__':
    res = []
    input = [3, 23, 4, 5, 4,32, 12, 234, 1, 1, 1, 2, 4, 4, 234, 45, 2, 23, 4, 23, 234, 54, 15, 4, 434, 2, 34, 2341, 745,
             124, 234, 24, 233, 45, 45, 44223, 23, 756]
    print(sorted(input))
    #print(kth_largest(2, [34,223,56,45]))
    #print(kth_largest(5, input))
    #print(kth_largest(8, input))
    #print(kth_largest(10, input))

    print(kth_largest_new(2, [1,2,3,4,5]))
    print(kth_largest_new(2, [34, 223, 56, 45]))
    print(kth_largest_new(5, input))
    print(kth_largest_new(8, input))
    print(kth_largest_new(10, input))

    #v = [1,2,3,4]
    #v.pop()
    #print(v)

