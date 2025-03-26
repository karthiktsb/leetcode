import heapq


def kth_largest(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


def kth_chatgpt(nums: list[int], k: int) -> int:
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        heapq.heappush(min_heap, num)
        heapq.heappop(min_heap)

    return min_heap[0]


def mine(nums, k):
    res = []

    for n in nums:
        if res and n > res[-1]:
            res.append(n)
            res.sort(reverse=True)
            if len(res) >= k:
                res.pop()
        else:
            res.append(n)

    return res[k - 1]



def func(l1):
    for x in l1:
        yield x * x


if __name__ == '__main__':
    print(kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(kth_chatgpt([3, 2, 1, 5, 6, 4, 7], 3))
    print(mine([3, 2, 1, 5, 6, 4, 7], 3))
    print(mine([3, 2, 1, 5, 6, 4, 7], 1))

    a = [(1, 2, 3, 4), (3, 7, 5, 2), (6, 4, 2, 3)]

    print(sorted(a, key=lambda x: x[1], reverse=True))
    a.sort(key=lambda x: x[1], reverse=True)
    print(a)

    b = "m"

    c = b if b == "n" else "an"

    print(c)

    arr = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9, 9, 7, 6, 6, 5, 5, 5]

    it = func(arr)

    try:
        while True:
            i = next(it)
            print(i)
    except StopIteration:
        pass

    print([x for x in arr if x % 2 == 0])

    dict1 = {"b": 1, "c": 2, "a": 5}

    print([k for (k, v) in dict1.items() if v >= 2])

    nums1 = [3,32,11,21,1,22,3,4]

    heapq.heapify(nums1)

    print(nums1)
