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


def main():
    nactena_data = read_data("sequential.json", "dna_sequence")
    target = "A"
    vysledek = linear_search(nactena_data, target)

    print(f"Hledane pismeno: {target}")
    print(f"Výsledek: {vysledek}")


if __name__ == '__main__':
    main()