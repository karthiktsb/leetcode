def sliding_window_max(input: list[int], k: int) -> list[int]:
    result = []
    deque = []

    for i in range(len(input)):
        while deque and deque[0] < i - k + 1:
            deque.pop(0)

        while deque and input[deque[-1]] < input[i]:
            deque.pop()

        deque.append(i)

        if i >= k - 1:
            result.append(input[deque[0]])

    return result


def sliding_window_with_max(input: list[int], k: int) -> list[int]:
    result = []

    for i in range(len(input)):
        if i >= k - 1:
            result.append(max(input[i - k + 1: i + 1]))

    return result


if __name__ == '__main__':
    print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(sliding_window_with_max([1, 3, -1, -3, 5, 3, 6, 7], 4))
