def count_removed_rolls(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    total_removed = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    while True:
        to_remove = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    adjacent_rolls = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '@':
                            adjacent_rolls += 1

                    if adjacent_rolls < 4:
                        to_remove.append((i, j))

        if not to_remove:
            break

        total_removed += len(to_remove)
        for i, j in to_remove:
            grid[i][j] = '.'

    return total_removed


def parse_input(input_text):
    return [list(line) for line in input_text.strip().split('\n') if line]

with open('input.txt', 'r') as file:
        input_text = file.read()
        print(count_removed_rolls(parse_input(input_text)))
