def product(nums):
    res = [0] * len(nums)

    res[0] = 1
    for i in range(1,len(nums)):
        res[i] = res[i - 1] * nums[i - 1]

    prev_prod = 1
    for i in range(len(nums) - 1, -1 ,-1):
        res[i] *= prev_prod
        prev_prod *= nums[i]

    return res


def sum(nums):
    res = [0] * len(nums)

    for i in range(1, len(nums)):
        res[i] = res[i - 1] + nums[i -1]

    prev_sum = 0
    for i in range(len(nums) -1, -1, -1):
        res[i] += prev_sum
        prev_sum += nums[i]

    return res


if __name__ == '__main__':
    print(product([1,2,3,4]))
    print(product([0, 1, 2, 3, 4]))
    print(sum([1, 2, 3, 4]))
    print(sum([0, 1, 2, 3, 4]))

