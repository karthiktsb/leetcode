import heapq


def lastStoneWeight(stones: list[int]) -> int:
    if len(stones) == 1:
        return stones[0]

    stones_heap = [-s for s in stones]

    heapq.heapify(stones_heap)

    while len(stones_heap) > 1:
        first = heapq.heappop(stones_heap)
        second = heapq.heappop(stones_heap)

        heapq.heappush(stones_heap, abs(first - second))

    if stones_heap:
        return abs(stones_heap[0])
    else:
        return 0


if __name__ == '__main__':
    print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print(lastStoneWeight([5]))
