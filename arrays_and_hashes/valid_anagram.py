def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    else:
        dict = {}
        for c in s:
            dict[c] = dict.get(c, 0) + 1

        for c in t:
            dict[c] = dict.get(c, 0) - 1

        res = [value for value in dict.values() if value != 0]

        if len(res) > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    print(valid_anagram("anagram", "nagaram"))
