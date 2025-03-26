def check_valid_string(s: str) -> bool:
    left_max, left_min = 0, 0

    for c in s:
        if c == "(":
            left_max += 1
            left_min += 1
        else:
            if c == ")":
                left_max -= 1
                left_min -= 1
            else:
                left_max += 1
                left_min -= 1

        if left_max < 0:
            return False

        if left_min < 0:
            left_min = 0

    return left_min == 0


def check_valid_string_stack(s: str) -> bool:
    left = []
    star = []

    for i, c in enumerate(s):
        if c == "(":
            left.append(i)
        elif c == "*":
            star.append(i)
        else:
            if not star and not left:
                return False
            else:
                if left:
                    left.pop()
                else:
                    star.pop()

    while star and left:
        if left.pop() > star.pop():
            return False

    return not left


if __name__ == '__main__':
    print(check_valid_string("((*))"))
    print(check_valid_string("((*)))"))
    print(check_valid_string("((*))))"))
    print(check_valid_string(")((*)))"))
    print(check_valid_string("(((()))())))*))())()(**(((())(()(*()((((())))*())(())*(*(()(*)))()*())**((()(()))())(*(*))*))())"))

    print(check_valid_string_stack("((*))"))
    print(check_valid_string_stack("((*)))"))
    print(check_valid_string_stack("((*))))"))
    print(check_valid_string_stack(")((*)))"))
    print(check_valid_string_stack(
        "(((()))())))*))())()(**(((())(()(*()((((())))*())(())*(*(()(*)))()*())**((()(()))())(*(*))*))())"))
    print(check_valid_string_stack(")"))