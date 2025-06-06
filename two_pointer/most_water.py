def most_water(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, curr_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == '__main__':
    print(most_water([1,8,6,2,5,4,8,3,7]))