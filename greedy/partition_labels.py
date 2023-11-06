def partitionLabels(s: str) -> list[int]:
    res = []
    size = 0
    end = 0

    char_indexes = {}

    for c in set(s):
        char_indexes[c] = s.rfind(c)

    for (i, c) in enumerate(s):
        size += 1
        end = max(end, char_indexes[c])

        if i == end:
            res.append(size)
            size = 0

    return res


if __name__ == '__main__':
    print(partitionLabels("ababcbacadefegdehijhklij"))
    print(partitionLabels("eccbbbbdec"))
    print(partitionLabels("eccbbbbd"))
    print(partitionLabels("abcdef"))