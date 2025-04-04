def word_break(s: str, wordDict: list[str]) -> bool:
    temp = s
    wordDict.sort(key=lambda x: len(x))

    for word in wordDict:
        while word in temp:
            temp = temp.replace(word, "")

    return temp == ""


def work_break_dp(s: str, wordDict: list[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[-1] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]


if __name__ =='__main__':
    #print(word_break("leetcode", ["leet", "code"]))
    #print(word_break("applepenapple", ["apple", "pen"]))
    #print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    #print(word_break("cars", ["cars", "ca", "rs"]))

    print(work_break_dp("leetcode", ["leet", "code"]))
    print(work_break_dp("applepenapple", ["apple", "pen"]))
    print(work_break_dp("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(work_break_dp("cars", ["cars", "ca", "rs"]))
    print(work_break_dp("aaaaaaa", ["aaaa", "aaa"]))