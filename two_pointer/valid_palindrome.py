def valid_palindrome(str):
    left = 0
    right = len(str) - 1

    while left < right:
        if str[left] != str[right]:
            return False

        left += 1
        right -= 1

    return True

if __name__ == '__main__':
    print(valid_palindrome("ababa"))
    print(valid_palindrome("ababab"))