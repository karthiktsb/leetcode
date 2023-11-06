def fibinocci(n: int):
    n1, n2 = 0, 1

    print(n1)
    print(n2)
    for i in range(n):
        temp = n1 + n2
        print(temp)
        n1 = n2
        n2 = temp


if __name__ == '__main__':
    fibinocci(7)
