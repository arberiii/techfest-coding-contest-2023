def count_increased_depths(file_path: str) -> int:
    increased = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    depths = [int(line) for line in lines]

    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increased += 1

    return increased


print(count_increased_depths("test.txt"))
