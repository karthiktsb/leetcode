def trap(height):
    trapped = 0
    left = 0
    right = len(height) - 1
    leftMax = 0
    rightMax = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] > leftMax:
                leftMax = height[left]
            else:
                trapped += leftMax - height[left]
            left += 1
        else:
            if height[right] > rightMax:
                rightMax = height[right]
            else:
                trapped += rightMax - height[right]
            right -= 1

    return trapped



if __name__ == '__main__':
    print(trap([0,2,0,3,1,0,1,3,2,1]))
    print(trap([4,2,0,3,2,5]))