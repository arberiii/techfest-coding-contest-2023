def get_highest_caloric_content(file_path: str) -> int:
    highest_caloric_content = 0
    current_warrior = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        if not line:
            if current_warrior > highest_caloric_content:
                highest_caloric_content = current_warrior
            current_warrior = 0
        else:
            current_warrior += int(line)

    return highest_caloric_content


print(get_highest_caloric_content("test.txt"))
