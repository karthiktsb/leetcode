def quick_sort(nums: list[int]):
    if len(nums) <= 1:
        return nums

    pivot = nums[-1]
    left = []
    right = []
    equal = []

    for n in nums:
        if n < pivot:
            left.append(n)
        else:
            if n > pivot:
                right.append(n)
            else:
                equal.append(n)

    return quick_sort(left) + equal + quick_sort(right)

def main():
    print(quick_sort([5, 4, 3, 2, 1]))
    print(quick_sort([5, -4, 3, -2, -1]))


main()