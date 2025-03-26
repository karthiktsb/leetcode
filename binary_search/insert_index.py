def insert_index(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
       mid = l + (r - l) // 2

       if target == nums[mid]:
           return mid
       else:
          if target > nums[mid]:
              l = mid + 1
          else:
              r = mid - 1

    return l


if __name__ == '__main__':
    print(insert_index([1,3,5,7,18], 9))
    print(insert_index([1, 3, 5, 7, 18], 19))
    print(insert_index([1, 3, 5, 7, 18], 0))
    print(insert_index([1, 3, 5, 7, 18], 2))