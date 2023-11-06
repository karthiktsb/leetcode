from collections import defaultdict

def character_replacement(s: str, k: int) -> int:
    seen = defaultdict(int)
    l, r  = 0, 0
    max_rep = 0

    while r < len(s):
        seen[s[r]] = 1 + seen[s[r]]
        max_value = max(seen.values())

        while r - l + 1 - max_value > k:
            seen[s[l]] = seen[s[l]] - 1
            l += 1

        max_rep = max(max_rep, r - l + 1)

        r += 1


    return max_rep


if __name__ == '__main__':
    print(character_replacement("AABABBAAAAAABAAAAA", 1))

