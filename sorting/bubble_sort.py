

def bubble_sort(nums:list[int]):
    n = len(nums)

    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


if __name__ == "__main__":
    print(bubble_sort([4,3,2,1,5,6,3,2,1]))