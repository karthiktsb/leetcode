from collections import defaultdict


def group_anagrams(strs):
    dict = defaultdict(list)

    for str in strs:
        str_sorted = ''.join(sorted(str))
        dict[str_sorted].append(str)

    return list(dict.values())


if __name__ == '__main__':
    print(group_anagrams(['tea', 'ate', 'eat', 'tm']))
    print("this is my new home".split(" "))

