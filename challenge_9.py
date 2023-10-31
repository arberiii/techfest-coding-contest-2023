SEABED = "."
CORAL_SHRINE = "#"
CORAL_FOREST = "|"


def count_adjacent_spans(x: int, y: int, state: list[list[str]]) -> tuple[int, int, int]:
    counts = {
        SEABED: 0,
        CORAL_SHRINE: 0,
        CORAL_FOREST: 0,
    }
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i < 0 or j < 0:
                continue
            if i >= len(state) or j >= len(state[i]):
                continue

            if (i, j) == (x, y):
                continue

            counts[state[i][j]] += 1
    return counts[SEABED], counts[CORAL_SHRINE], counts[CORAL_FOREST]


def get_new_span_state(current_state: list[list[str]]) -> list[list[str]]:
    new_state = [row.copy() for row in current_state]

    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            seabed_count, coral_shrine_count, coral_fores_count = count_adjacent_spans(i, j, current_state)
            if current_state[i][j] == CORAL_SHRINE:
                if coral_shrine_count > 0 and coral_fores_count > 0:
                    new_state[i][j] = CORAL_SHRINE
                else:
                    new_state[i][j] = SEABED
            elif current_state[i][j] == SEABED:
                if coral_fores_count >= 3:
                    new_state[i][j] = CORAL_FOREST
            elif current_state[i][j] == CORAL_FOREST:
                if coral_shrine_count >= 3:
                    new_state[i][j] = CORAL_SHRINE

    return [row.copy() for row in new_state]


def get_total_mystical_power(file_path: str, tide_cycles) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    current_state = [[char for char in line] for line in lines]

    for _ in range(tide_cycles):
        current_state = get_new_span_state(current_state)

    counts = {
        SEABED: 0,
        CORAL_SHRINE: 0,
        CORAL_FOREST: 0,
    }
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            counts[current_state[i][j]] += 1

    return counts[CORAL_SHRINE] * counts[CORAL_FOREST]


print(get_total_mystical_power("test.txt", 10))
