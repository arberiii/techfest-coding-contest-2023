def get_final_destination(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    current_position = "E"
    location = {"E": 0, "N": 0, "W": 0, "S": 0}
    directions = ["N", "E", "S", "W"]
    for line in lines:
        line = line.strip()
        action = line[0]
        value = int(line[1:])
        if action == "F":
            location[current_position] += value
        elif action == "N":
            location["N"] += value
        elif action == "S":
            location["S"] += value
        elif action == "E":
            location["E"] += value
        elif action == "W":
            location["W"] += value
        elif action == "R":
            current_position = directions[(directions.index(current_position) + int(value / 90)) % 4]
        elif action == "L":
            current_position = directions[(directions.index(current_position) - int(value / 90)) % 4]

    return abs(location["N"] - location["S"]) + abs(location["E"] - location["W"])


print(get_final_destination("test.txt"))
