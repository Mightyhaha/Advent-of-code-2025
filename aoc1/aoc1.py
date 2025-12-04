def count_zero_rotations(lines):
    pos = 50
    count = 0
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        dirc = line[0].upper()
        try:
            dist = int(line[1:])
        except Exception:
            continue
        if dirc == 'L':
            pos = (pos - dist) % 100
        elif dirc == 'R':
            pos = (pos + dist) % 100
        else:
            continue
        if pos % 100 == 0:
            count += 1
    return count

def count_zero_passes(lines):
    pos = 50
    count = 0
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        dirc = line[0].upper()
        try:
            dist = int(line[1:])
        except Exception:
            continue

        if dirc == 'L':
            minimal_k = pos if pos != 0 else 100
            if dist >= minimal_k:
                count += 1 + (dist - minimal_k) // 100
            pos = (pos - dist) % 100
        elif dirc == 'R':
            minimal_k = (100 - pos) if pos != 0 else 100
            if dist >= minimal_k:
                count += 1 + (dist - minimal_k) // 100
            pos = (pos + dist) % 100
        else:
            continue

    return count


def main():
    with open('dial.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(count_zero_passes(lines))


if __name__ == '__main__':
    main()
