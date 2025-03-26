def checkInclusion(s1: str, s2: str) -> bool:
    if s1 and s2 and len(s2) >= len(s1):
        l1 = len(s1)
        s1_sorted = "".join(sorted(s1))

        for i in range(len(s2) - len(s1) + 1):
            if s1_sorted == "".join(sorted(s2[i:i + l1])):
                return True

    return False


def check_inclusion(s1: str, s2: str):
    l1 = len(s1)
    l2 = len(s2)

    if l1 > l2:
        return False

    l1_total = 0
    for c in s1:
        l1_total += hash(c)

    l, r = 0, 0

    l2_total = 0
    while r < l1:
        l2_total += hash(s2[r])
        r += 1

    while r < l2:
        if l1_total == l2_total:
            return True
        l2_total += hash(s2[r])
        l2_total -= hash(s2[l])
        l += 1
        r += 1

    if l1_total == l2_total:
        return True

    return False


if __name__ == '__main__':
    print(check_inclusion1("abz", "basdasdasdxfxfddvbdsadasdbaz"))
    print(checkInclusion("ab", "dsfkjlkjladba"))
    print(check_inclusion("abzm", "basdasdasdxfxfddvbdsadasdbaz"))
    print(check_inclusion("ab", "dsfkjlkjladba"))
    print(check_inclusion("abz", "zbadasdasdxfxfddvbdsadasdba"))
    print(check_inclusion("abc", "ccccbbbbaaaa"))
    print(check_inclusion("aba", "ccccbbbbaaaa"))
    #l = ""

    #if l:
    #    print("Non Empty List")
    #else:
    #    print("Empty list")
