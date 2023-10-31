from collections import defaultdict


def get_decoded_coordinates(file_path: str) -> str:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    words = []
    for line in lines:
        words.append([char for char in line])

    secret = ""
    for i in range(len(words[0])):
        d = defaultdict(int)
        for j in range(len(words)):
            d[words[j][i]] += 1

        secret += max(d, key=d.get)

    return secret


print(get_decoded_coordinates("test.txt"))
