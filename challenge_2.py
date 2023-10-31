def is_tree_visible_in_north(forest: list[list[int]], x: int, y: int) -> bool:
    for north in range(x - 1, -1, -1):
        if forest[north][y] >= forest[x][y]:
            return False
    return True


def is_tree_visible_in_south(forest: list[list[int]], x: int, y: int) -> bool:
    for south in range(x + 1, len(forest)):
        if forest[south][y] >= forest[x][y]:
            return False
    return True


def is_tree_visible_in_west(forest: list[list[int]], x: int, y: int) -> bool:
    for west in range(y - 1, -1, -1):
        if forest[x][west] >= forest[x][y]:
            return False
    return True


def is_tree_visible_in_east(forest: list[list[int]], x: int, y: int) -> bool:
    for east in range(y + 1, len(forest[x])):
        if forest[x][east] >= forest[x][y]:
            return False
    return True


def is_tree_visible(forest: list[list[int]], x: int, y: int) -> bool:
    return (
            is_tree_visible_in_north(forest, x, y)
            or is_tree_visible_in_south(forest, x, y)
            or is_tree_visible_in_west(forest, x, y)
            or is_tree_visible_in_east(forest, x, y)
    )


def count_visible_trees(file_path: str) -> int:
    visible_trees = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    forest = []
    for line in lines:
        forest.append([int(i) for i in line])

    for i in range(len(forest)):
        for j in range(len(forest[i])):
            if is_tree_visible(forest, i, j):
                visible_trees += 1

    return visible_trees


print(count_visible_trees("test.txt"))
