def valid_paranthesis(s: str) -> bool:
    dict = {"}": "{", "]": "[", ")": "("}
    stack = []

    for c in s:
        if c in dict:
            if stack:
                element = stack.pop()
                if element != dict[c]:
                    return False
            else:
                return False
        else:
            stack.append(c)

    return True


if __name__ == '__main__':
    print(valid_paranthesis('{}()[]}{'))
    print(valid_paranthesis('{[()]}'))
    print(valid_paranthesis('){[()]}'))


