def top_k_frequent(nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        print(freq)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == '__main__':
    print(top_k_frequent([1,1,2,2,1,1,3,3,2,2,6], 2))

    d = {1: 4, 2: 5, 3: 4}
    topk = 4
    res = [k for k, v in d.items() if v == topk]
    res1 = list(map(lambda x: x * 2, res))
    res2 = list(filter(lambda x: x > 2, res))
    print(res)
    print(res1)
    print(res2)


