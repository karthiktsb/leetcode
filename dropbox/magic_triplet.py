

# O(n^2 + n log n)
def magic_triplet(nums: list[int]):
    nums.sort()
    res = []

    for i in range(len(nums) - 3):
        l = i + 1
        r = len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            else:
                if total < 0:
                    l += 1
                else:
                    r -= 1

    return res


# O(n^3)
def magic_triplet_brute_force(nums: list[int]):
    result = []

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result

def magic_triplet_back_tracking(nums: list[int]):
    result = []

    def dfs(path: list[int], total: int, index: int):
        if len(path) == 3:
            if total == 0:
                result.append(path.copy())
            return

        if index < len(nums):
            path.append(nums[index])
            dfs(path, total + nums[index], index + 1)
            path.pop()
            dfs(path, total, index + 1)

    dfs([], 0, 0)
    return result





if __name__ == "__main__":
    print(magic_triplet([10, 3, -4, 1, -6, 9]))
    print(magic_triplet_brute_force([10, 3, -4, 1, -6, 9]))
    print(magic_triplet_back_tracking([10, 3, -4, 1, -6, 9]))



