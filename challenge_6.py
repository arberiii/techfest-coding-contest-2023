def get_product_of_two_numbers_that_sum_to_1999(file_path: str) -> int:
    target_sum = 1999
    seen_numbers = set()

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        number = int(line)
        if (target_sum - number) in seen_numbers:
            return number * (target_sum - number)
        seen_numbers.add(number)

    return -1


print(get_product_of_two_numbers_that_sum_to_1999(("test.txt")))
