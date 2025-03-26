def longest_seq(nums):
    res = 0
    for i in nums:
        if i - 1 not in nums:
            c = i
            curseq = 0
            while c in nums:
                c += 1
                curseq += 1

            res = max(res, curseq)

    return res


if __name__ == '__main__':
    print(longest_seq([99,100,4,200,1,3,2,103,104,102,101,105,106,107]))
