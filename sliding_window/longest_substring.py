def longest(s: str) -> int:
    seen = []
    l, r = 0, 0
    max_length = 0

    while r < len(s):
        if s[r] not in seen:
            seen.append(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1
        else:
            seen.remove(s[l])
            l += 1

    return max_length

if __name__ == '__main__':
    print(longest("abacdaefabm"))