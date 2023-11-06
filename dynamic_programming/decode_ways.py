def decode_ways(s: str) -> int:
    next, next_two = 0, 1

    if s[-1] != "0":
        next = 1

    for i in range(len(s) - 2, -1, -1):
        temp = next
        curr = s[i: i + 2]

        if s[i] != '0':
            if curr >= "10" and curr <= "26":
                next = next + next_two
        else:
            next = 0

        next_two = temp

    return next


if __name__ == '__main__':
    print(decode_ways("127"))
    print(decode_ways("126"))