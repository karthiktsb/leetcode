

# O(n^2 + n log n)
def magic_triplet(nums: list[int]):
    nums_sorted = sorted(nums)
    result = []

    for i in range(len(nums_sorted) - 3):
        l = i + 1
        r = len(nums_sorted) - 1

        while l < r:
            summed = nums_sorted[i] + nums_sorted[l] + nums_sorted[r]

            if summed == 0:
               result.append([nums_sorted[i], nums_sorted[l], nums_sorted[r]])
               l += 1
               r -= 1
            else:
                if summed < 0:
                    l += 1
                else:
                    r -= 1

    return result


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

    def dfs(path: list[int], index: int, summed: int):
        if len(path) == 3:
            if summed == 0:
                result.append(path.copy())
            return

        if index < len(nums):
            path.append(nums[index])
            dfs(path, index + 1, summed + nums[index])
            path.pop()
            dfs(path, index + 1, summed)

    dfs([], 0, 0)

    return result


if __name__ == "__main__":
    print(magic_triplet([10, 3, -4, 1, -6, 9]))
    print(magic_triplet_brute_force([10, 3, -4, 1, -6, 9]))
    print(magic_triplet_back_tracking([10, 3, -4, 1, -6, 9]))



