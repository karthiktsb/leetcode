def top_k_elements(nums, k):
    dict = {}

    for i in nums:
        dict[i] = dict.get(i, 0) + 1

    sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    return [k for k, v in sorted_items][:k]


if __name__ == '__main__':
    print(top_k_elements([1,1,1,2,2,3,3,3,3,3,3,3,3,2,2,2,2,1,1,1,1,1], 2))