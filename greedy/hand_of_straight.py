from collections import defaultdict


def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size != 0:
        return False

    hold = defaultdict(int)

    for i in hand:
        hold[i] = hold[i] + 1

    groups = len(hand) // group_size

    for i in range(groups):
        start = min(hold.keys())

        for j in range(start, start + group_size):
            if j not in hold:
                return False

            if hold[j] == 1:
                hold.pop(j)
            else:
                hold[j] = hold[j] - 1

    return True


if __name__ == '__main__':
    print(is_n_straight_hand([8, 10, 12], 3))
    print(is_n_straight_hand([2, 1], 2))
    print(is_n_straight_hand([1], 1))
    print(is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
    print(is_n_straight_hand([1, 2, 3, 6, 2, 3, 5, 7, 8], 3))
    print(is_n_straight_hand([1, 2, 3, 4, 5, 6], 4))
