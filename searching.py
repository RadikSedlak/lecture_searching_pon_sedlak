from pathlib import Path


import time
import matplotlib.pyplot as plt
from generator import ordered_sequences


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


sizes = [100, 500, 1000, 5000, 10000]

linear_times = []
binary_times = []

for size in sizes:
    data = ordered_sequences(size)
    target = data[-1]

    start = time.perf_counter()
    result_linear = linear_search(data, target)
    end = time.perf_counter()
    linear_times.append(end - start)

    start = time.perf_counter()
    result_binary = binary_search(data, target)
    end = time.perf_counter()
    binary_times.append(end - start)

    print("size:", size)
    print("linear result:", result_linear)
    print("binary result:", result_binary)
    print("---")

plt.plot(sizes, linear_times, label="linear search")
plt.plot(sizes, binary_times, label="binary search")

plt.xlabel("velikost vstupu")
plt.ylabel("čas (sekundy)")
plt.title("Porovnání rychlosti vyhledávání")
plt.legend()

plt.show()