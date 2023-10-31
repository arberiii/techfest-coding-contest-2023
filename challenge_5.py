def count_etched_triangles(file_path: str) -> int:
    triangles = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        sides = [int(x) for x in line.split()]

        a, b, c = sides
        if a + b > c and a + c > b and b + c > a:
            triangles += 1

    return triangles


print(count_etched_triangles("test.txt"))
