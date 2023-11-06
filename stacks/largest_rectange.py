def largest_rectangle_area(heights: list[int]) -> int:
    max_area = 0
    stack = []

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack and heights[i] < heights[stack[-1]]:
        height = heights[stack[-1]]
        if stack:
            width = len(heights) - stack[-1] -1
        else:
            width = len(heights)
        max_area = max(max_area, height * width)

    return max_area

if __name__ == '__main__':
    print(largest_rectangle_area([2,1,5,6,2,3]))

