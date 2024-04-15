def letterCombinations(digits: str) -> list[str]:
    res = []
    dict1 = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    def dfs(path: str, index: int):
        if index >= len(digits):
            res.append(path)
            return

        lkp = dict1.get(digits[index])

        for i in lkp:
            dfs(path + i, index + 1)


    dfs("",0)
    return res


if __name__ == '__main__':
    print(letterCombinations("23"))
    print(letterCombinations("2"))
    print(letterCombinations(""))
    print(letterCombinations("256"))
    print(letterCombinations("99"))
