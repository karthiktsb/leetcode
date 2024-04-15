def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    else:
        dict1 = {}

        for c in s:
            dict1[c] = dict1.get(c, 0) + 1

        for c in t:
            dict1[c] = dict1.get(c, 0) - 1

        res = [k for k, v in dict1.items() if v != 0]

        if res:
            return False
        else:
            return True


if __name__ == '__main__':
    print(valid_anagram("anagram", "nagaram"))
    print(valid_anagram("anagram", "nagaran"))
