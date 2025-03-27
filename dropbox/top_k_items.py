def get_top_k_elements(nums: list[int], k: int):
    if len(nums) <= k:
        return nums

    res = []

    def insert_index(l1: list[int], target: int):
        l = 0
        r = len(l1) - 1

        while l <= r:
            m = l + (r - l) // 2

            if l1[m] == target:
                return m
            else:
                if target > l1[m]:
                    l = m + 1
                else:
                    r = m - 1

        return l

    for n in nums:
        if res:
            if n >= res[0]:
                index = insert_index(res, n)
                res.insert(index, n)
                if len(res) > k:
                    res.pop(0)
        else:
            res.append(n)

    return res


if __name__ == "__main__":
    print(get_top_k_elements([1,2,3,4,5], 2))
    print(get_top_k_elements([1, 5, 4, 4, 2, 6, 1, 0, 3, 9], 2))
    print(get_top_k_elements([4,4,4,4,4], 3))
    print(get_top_k_elements([4, 4, 4, 4, 4, 7, 6, 3], 4))

    assert get_top_k_elements([1, 5, 4, 4, 2, 6, 1, 0, 3, 9], 2) == [6, 9]
    assert get_top_k_elements([-1, -5, -4, -4, -2, -6, -1, 0, -3, -9], 2) == [-1, 0]
    assert get_top_k_elements([4,4,4,4,4], 3) == [4]