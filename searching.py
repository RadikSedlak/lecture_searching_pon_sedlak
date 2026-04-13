from pathlib import Path
import json

def read_data(filename, field):
    f = open(filename, "r", encoding="utf-8")
    data = json.load(f)
    f.close()

    if field in data:
        return data[field]
    return None


def linear_search(sequence, target):
    positions = []
    i = 0

    for item in sequence:
        if item == target:
            positions.append(i)
        i = i + 1

    return {"positions": positions, "count": len(positions)}


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
    data = read_data("sequential.json", "ordered_numbers")
    target = 5

    if data is None:
        print("chyba")
        return

    result = binary_search(data, target)
    print(result)


if __name__ == "__main__":
    main()


