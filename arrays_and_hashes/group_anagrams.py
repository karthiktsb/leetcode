from collections import defaultdict
def group_anagrams(strs):
    res = defaultdict(list)

    for str in strs:
        sorted_word = ''.join(sorted(str))
        res[sorted_word].append(str)

    return list(res.values())

if __name__ == '__main__':
    print(group_anagrams(['tea', 'ate', 'eat', 'tm']))
    print("this is my new home".split(" "))

