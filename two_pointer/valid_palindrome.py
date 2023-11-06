def valid_palindrome(str):
    left = 0
    right = len(str) - 1

    while (left < right):
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False

    return True


if __name__ == '__main__':
    print(valid_palindrome("ababa"))
    print(valid_palindrome("ababab"))