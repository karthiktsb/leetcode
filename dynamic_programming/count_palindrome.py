def count_palindome(s: str) -> int:
    res = 0

    def count_palindrome(l: int, r: int):
        nonlocal res, s
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

    for i in range(len(s)):
        for l, r in ((i, i), (i, i + 1)):
            count_palindrome(l, r)

    return res


def list_palindome(s: str) -> list[str]:
    res = []

    def count_palindrome(l, r):
        nonlocal s, res
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res.append(s[l: r + 1])
            l -= 1
            r += 1

    for i in range(len(s)):
        for l, r in ((i, i), (i, i + 1)):
            count_palindrome(l, r)


    return res

if __name__ == '__main__':
    print(count_palindome("aaa"))
    print(count_palindome("abcddcbd"))
    print(list_palindome("aaa"))
    print(list_palindome("abcddcbd"))

