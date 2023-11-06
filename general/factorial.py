def factorial(n: int):
    temp = 1
    for i in range(1, n + 1):
        temp = temp * i
        print(temp)


if __name__ == '__main__':
    print(factorial(10))