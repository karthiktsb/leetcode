def get_top_k_elements(nums: list[int], k: int):
    if len(nums) <= k:
        return nums

    result = []

    def get_insert_index(res: list[int], num: int):
        l = 0
        r = len(res) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if res[mid] == num:
                return mid
            else:
                if res[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
        return l

    for i in nums:
        if not result:
            result.append(i)
        else:
            if i > result[0]:
                index = get_insert_index(result, i)
                result.insert(index, i)
                if len(result) > k:
                    result.pop(0)

    return result


if __name__ == "__main__":
    print(get_top_k_elements([1,2,3,4,5], 2))
    print(get_top_k_elements([1, 5, 4, 4, 2, 6, 1, 0, 3, 9], 2))
    print(get_top_k_elements([4,4,4,4,4], 3))

    assert get_top_k_elements([1, 5, 4, 4, 2, 6, 1, 0, 3, 9], 2) == [6, 9]
    assert get_top_k_elements([-1, -5, -4, -4, -2, -6, -1, 0, -3, -9], 2) == [-1, 0]
    assert get_top_k_elements([4,4,4,4,4], 3) == [4]
