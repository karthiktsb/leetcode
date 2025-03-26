def insertion_sort(nums:list[int]):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


def main():
    print(insertion_sort([5,4,3,2,1]))


main()