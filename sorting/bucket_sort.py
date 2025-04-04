def bucket_sort(nums: list[int]):
    if not nums:
        return nums

    length = len(nums)
    maxv, minv = max(nums), min(nums)

    bucket_range = (maxv - minv) / length
    buckets = [[] for _ in range(length)]

    for n in nums:
        if n == maxv:
            idx = length - 1
        else:
            idx = int((n - minv) / length)
        buckets[idx].append(n)

    for bucket in buckets:
        bucket.sort()

    res = []
    for bucket in buckets:
        res.extend(bucket)

    return res


def main():
    print(bucket_sort([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,-1]))
    print(bucket_sort([15, 13, 12, 10, 8, 7, 5, 4, 2, 1, 0, -1]))


main()
