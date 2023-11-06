def top_k_elements(nums, k):
    dict={}

    for i in nums:
        dict[i] = dict.get(i, 0) + 1

    res = sorted(dict.items(), key=lambda item: item[1], reverse=True)

    return [key for key, value in res[:k]]

if __name__ == '__main__':
    print(top_k_elements([1,1,1,2,2,3,3,3,3,3,3,3,3,2,2,2,2], 2))