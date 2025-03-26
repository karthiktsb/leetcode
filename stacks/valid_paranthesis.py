def valid_parenthesis(s: str) -> bool:
    dict1 = {"}": "{", "]": "[", ")": "("}
    stack = []

    for c in s:
        if c in dict1:
            if stack:
                elem = stack.pop()
                if elem != dict1[c]:
                    return False
            else:
                return False
        else:
            stack.append(c)

    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    print(valid_parenthesis('{}()[]}{'))
    print(valid_parenthesis('{[()]}'))
    print(valid_parenthesis('){[()]}'))


