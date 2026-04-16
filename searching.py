import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        if field in data:
            return data[field]

def linear_search(sekvence, number):
    positions = []

    for i, item in enumerate(sekvence):
        if item == number:
            positions.append(i)

    return {
        "positions": positions, "count": len(positions)
    }


def binary_search(seznam, hledane_cislo):
    left = 0
    right = len(seznam) - 1

    while left <= right:
        middle = (left + right) // 2
        prvek_ve_stredu = seznam[middle]
        if prvek_ve_stredu == hledane_cislo:
            return middle
        elif prvek_ve_stredu < hledane_cislo:
            left = middle + 1
        else:
            right = middle - 1

    return None

def main():
    nactena_data = read_data("sequential.json", "unordered_numbers")
    target = 14
    vysledek = linear_search(nactena_data, target)

    print(f"Hledane cislo: {target}")
    print(f"Vysledek: {vysledek}")

    nactena_data2 = read_data("sequential.json", "ordered_numbers")
    binarni = binary_search(nactena_data2, target)
    print(binarni)

if __name__ == '__main__':
    main()