def fibinocci(n: int):
    fib = [0, 1]

    if n == 1:
        return 0
    else:
        for i in range(2, n):
            next_seq = fib[-1] + fib[-2]
            fib.append(next_seq)
            print(fib)
        return fib[-1]

if __name__ == '__main__':
    print(fibinocci(7))
