import heapq


def lastStoneWeight(stones: list[int]) -> int:
    while len(stones) > 1:
        stones.sort()

        cur = stones.pop() - stones.pop()

        if cur:
            stones.append(cur)

    return stones[0] if stones else 0


if __name__ == '__main__':
    print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print(lastStoneWeight([5]))
