def parse_grid(lines, part=1):
    lines = [line.rstrip("\n") for line in lines if line.rstrip("\n") != ""]
    if not lines:
        return 0

    maxlen = max(len(line) for line in lines)
    grid = [line.ljust(maxlen) for line in lines]
    n_rows = len(grid)
    op_row = grid[-1]

    results = []
    col = 0
    while col < maxlen:
        if all(grid[r][col] == ' ' for r in range(n_rows)):
            col += 1
            continue

        start = col
        while col < maxlen and not all(grid[r][col] == ' ' for r in range(n_rows)):
            col += 1
        end = col - 1

        op = op_row[start:end+1].strip()
        if not op:
            continue
        op_char = op[0]

        nums = []
        if part == 1:
            for r in range(n_rows - 1):
                s = grid[r][start:end+1].strip()
                if s:
                    try:
                        nums.append(int(s))
                    except ValueError:
                        pass
        else:
            for c in range(end, start - 1, -1):
                # Build the vertical digits for this column, remove all spaces
                col_digits = ''.join(grid[r][c] for r in range(n_rows - 1)).replace(' ', '')
                if col_digits:
                    try:
                        nums.append(int(col_digits))
                    except ValueError:
                        pass

        if not nums:
            continue

        if op_char == '+':
            res = sum(nums)
        elif op_char == '*':
            try:
                from math import prod
                res = prod(nums)
            except Exception:
                res = 1
                for v in nums:
                    res *= v
        else:
            continue

        results.append(res)

    return sum(results)


with open("input.txt", "r") as f:
    lines = f.readlines()
print(parse_grid(lines, part=1))
print(parse_grid(lines, part=2))
