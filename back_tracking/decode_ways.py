class Solution:
    def num_decodings(self, s: str) -> int:
        lkp = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H','9': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O','16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V','23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}
        result = 0

        def dfs(path: str, index: int):
            nonlocal result
            if index >= len(s):
                result += 1
                return

            if s[index] in lkp:
                dfs(path + lkp[s[index]], index + 1)

            if index < len(s) - 1 and s[index] + s[index + 1] in lkp:
                dfs(path + lkp[s[index] + s[index + 1]], index + 2)

        dfs("", 0)
        return result


def main():
    fix = Solution()

    print(fix.num_decodings("12"))
    print(fix.num_decodings("123"))


main()
