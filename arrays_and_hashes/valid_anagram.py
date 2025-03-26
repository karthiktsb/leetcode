def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    dict = {}

    for c in s:
        dict[c] = dict.get(c,0) + 1

    for c in t:
        dict[c] = dict.get(c, 0) - 1

    res = [v for k,v in dict.items() if v != 0]

    if res:
        return False
    else:
        return True


if __name__ == '__main__':
    print(valid_anagram("anagram", "nagaram"))
    print(valid_anagram("anagram", "nagaran"))
