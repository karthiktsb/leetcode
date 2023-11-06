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
