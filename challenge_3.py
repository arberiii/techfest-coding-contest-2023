def has_two_same_adjacent_digits(number) -> bool:
    s = str(number)
    return any(s[i] == s[i + 1] for i in range(len(s) - 1))


def is_non_decreasing(number) -> bool:
    s = str(number)
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))


def count_eligible_codes(file_path: str) -> int:
    good_codes = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    lower_bound, upper_bound = map(int, lines[0].split("-"))

    for i in range(lower_bound, upper_bound + 1):
        if has_two_same_adjacent_digits(i) and is_non_decreasing(i):
            good_codes += 1

    return good_codes


print(count_eligible_codes("test.txt"))
