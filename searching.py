import json
import time
import matplotlib.pyplot as plt
from generators import ordered_sequence


def read_data(filename, field):
    f = open(filename, "r", encoding="utf-8")
    data = json.load(f)
    f.close()

    if field in data:
        return data[field]
    return None


def linear_search(sequence, target):
    i = 0

    for number in sequence:
        if number == target:
            return i
        i = i + 1

    return None


def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        middle = (left + right) // 2

        if sequence[middle] == target:
            return middle
        elif sequence[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None


def main():
    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []

    for size in sizes:
        data = ordered_sequence(size)
        target = data[-1]

        start = time.perf_counter()
        linear_search(data, target)
        linear_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        binary_search(data, target)
        binary_times.append(time.perf_counter() - start)

        print("size:", size)

    plt.plot(sizes, linear_times, label="linear search")
    plt.plot(sizes, binary_times, label="binary search")

    plt.xlabel("velikost vstupu")
    plt.ylabel("čas [s]")
    plt.title("porovnání vyhledávání")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()