def checkInclusion(s1: str, s2: str) -> bool:
    if s1 and s2 and len(s2) >= len(s1):
        s1_sorted = ''.join(sorted(s1))
        l = len(s1)
        for i in range(len(s2) - len(s1) + 1):
            if s1_sorted == ''.join(sorted(s2[i: i + l])):
                return True

    return False


if __name__ == '__main__':
    print(checkInclusion("ab", "basdasdasdxfxfddvbdsadasd"))
    print(checkInclusion("ab", "dsfkjlkjladba"))
    l = ""

    if l:
        print("Non Empty List")
    else:
        print("Empty list")
