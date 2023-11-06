def search(nums: list[list[int]], target: int) -> int:
    m = len(nums)
    n = len(nums[0])
    left = 0
    right = m * n - 1

    while (left <= right):
        mid = int(left + (right - left) / 2)
        mid_value = nums[int(m / n)][int(m % n)]

        if mid_value == target:
            return True
        else:
            if target > mid_value:
                left = mid + 1
            else:
                right = mid - 1


    return False

if __name__ == '__main__':
    print(search([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 7))

