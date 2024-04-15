def check_valid_string(s: str) -> bool:
    left_max, left_min = 0, 0
    i = 0

    while i < len(s) and left_max >= 0:
        if s[i] == "(":
            left_min += 1
            left_max += 1
        else:
            if s[i] == ")":
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1

        if left_min < 0:
            left_min = 0

        i += 1

    if left_max < 0:
        return False
    else:
        return left_min == 0



if __name__ == '__main__':
    print(check_valid_string("((*))"))
    print(check_valid_string("((*)))"))
    print(check_valid_string("((*))))"))
    print(check_valid_string(")((*)))"))
    print(check_valid_string("(((()))())))*))())()(**(((())(()(*()((((())))*())(())*(*(()(*)))()*())**((()(()))())(*(*))*))())"))
