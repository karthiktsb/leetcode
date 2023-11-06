def two_sum(nums, target):
    dict = {}
    for (i, v) in enumerate(nums):
        if target - v in dict:
            return [dict[target - v], i]
        else:
            dict[v] = i
    return []

if __name__ == '__main__':
    print(two_sum([11,15,11,33,3,22,44,56,677,55,43,33,33,33,6], 9))
    print(two_sum([11,15,11,33,22,44,56,677,55,43,33,33,33,3,6], 9))
    print(two_sum([1,3], 9))