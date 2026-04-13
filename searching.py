from pathlib import Path
import json

def read_data(filename, field):
    f = open(filename, "r", encoding="utf-8")
    data = json.load(f)
    f.close()

    if field in data:
        return data[field]
    else:
        return None




def linear_search(sequence, target):
    positions = []
    i = 0

    for item in sequence:
        if item == target:
            positions.append(i)
        i = i + 1

    return {"positions": positions, "count": len(positions)}


def main():
    data = read_data("sequential.json", "unordered_numbers")
    target = 5

    result = linear_search(data, target)
    print(result)


if __name__ == "__main__":
    main()