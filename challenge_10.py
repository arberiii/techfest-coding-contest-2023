from typing import Optional


def get_lines_from_movements(movement: list[tuple[str, int]]) -> list:
    lines = []
    start_point = (0, 0)
    next_point = (0, 0)
    for move in movement:
        direction = move[0]
        distance = move[1]
        if direction == "U":
            next_point = (start_point[0], start_point[1] + distance)
            lines.append((start_point, next_point))
        elif direction == "D":
            next_point = (start_point[0], start_point[1] - distance)
            lines.append((start_point, next_point))
        elif direction == "L":
            next_point = (start_point[0] - distance, start_point[1])
            lines.append((start_point, next_point))
        elif direction == "R":
            next_point = (start_point[0] + distance, start_point[1])
            lines.append((start_point, next_point))

        start_point = next_point
    return lines


def intersection_point(line_1: list, line_2: list) -> Optional[tuple[int, int]]:
    def is_point_outside_line(point: tuple[int, int], line: list):
        if min(line[0][0], line[1][0]) > point[0] or max(line[0][0], line[1][0]) < point[0]:
            return True

        if min(line[0][1], line[1][1]) > point[1] or max(line[0][1], line[1][1]) < point[1]:
            return True

        return False

    xdiff = (line_1[0][0] - line_1[1][0], line_2[0][0] - line_2[1][0])
    ydiff = (line_1[0][1] - line_1[1][1], line_2[0][1] - line_2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line_1), det(*line_2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    if is_point_outside_line((x, y), line_1):
        return None

    if is_point_outside_line((x, y), line_2):
        return None

    return x, y


def closest_distance_from_central_seal(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    first_movements = [(line[0], int(line[1:])) for line in lines[0].split(",")]
    second_movements = [(line[0], int(line[1:])) for line in lines[1].split(",")]

    first_lines = get_lines_from_movements(first_movements)
    second_lines = get_lines_from_movements(second_movements)

    minimum_distance = float('inf')
    for l_1 in first_lines:
        for l_2 in second_lines:
            intersection = intersection_point(l_1, l_2)
            if intersection is not None:
                distance = abs(intersection[0]) + abs(intersection[1])
                if distance < minimum_distance:
                    minimum_distance = distance

    return int(minimum_distance)


print(closest_distance_from_central_seal("test.txt"))
