import multiprocessing


def calculate_square(num):
    return num ** 2


if __name__ == "__main__":
    num_process = 4

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with multiprocessing.Pool(processes=num_process) as pool:
        results = pool.map(calculate_square, numbers)

    print(results)

