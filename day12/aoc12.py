from collections import defaultdict
import sys
import re


def parse_input(text):
    lines = [l.rstrip('\n') for l in text.splitlines()]
    shapes = {}
    regions = []

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if re.match(r'^\d+x\d+\s*:', line):
            break
        m = re.match(r'^(\d+)\s*:\s*$', line)
        if m:
            idx = int(m.group(1))
            i += 1
            shape_lines = []
            while i < n and lines[i].strip() != '' and not re.match(r'^\d+\s*:', lines[i].strip()) and not re.match(r'^\d+x\d+\s*:', lines[i].strip()):
                shape_lines.append(lines[i])
                i += 1
            # extract '#' positions
            coords = set()
            for y, row in enumerate(shape_lines):
                for x, ch in enumerate(row):
                    if ch == '#':
                        coords.add((x, y))
            if not coords:
                shapes[idx] = frozenset()
            else:
                # normalize to origin
                minx = min(x for x, y in coords)
                miny = min(y for x, y in coords)
                norm = frozenset(((x - minx, y - miny) for x, y in coords))
                shapes[idx] = norm
        else:
            i += 1

    while i < n:
        line = lines[i].strip()
        i += 1
        if not line:
            continue
        m = re.match(r'^(\d+)x(\d+)\s*:\s*(.*)$', line)
        if not m:
            continue
        w = int(m.group(1))
        h = int(m.group(2))
        counts = [int(x) for x in m.group(3).strip().split() if x != '']
        regions.append((w, h, counts))

    return shapes, regions


def orientations(shape):
    res = set()
    coords = list(shape)

    def normalize(cs):
        minx = min(x for x, y in cs)
        miny = min(y for x, y in cs)
        return frozenset(((x - minx, y - miny) for x, y in cs))

    for flipx in (False, True):
        for rot in range(4):
            cs = coords
            pts = []
            for x, y in cs:
                # flip horizontally
                if flipx:
                    x = -x
                # rotate around origin
                for _ in range(rot):
                    x, y = -y, x
                pts.append((x, y))
            res.add(normalize(pts))
    return list(res)


def generate_placements(orient, W, H):
    xs = [x for x, y in orient]
    ys = [y for x, y in orient]
    w = max(xs) + 1
    h = max(ys) + 1
    placements = []
    for ox in range(W - w + 1):
        for oy in range(H - h + 1):
            pts = tuple(((ox + x, oy + y) for x, y in orient))
            placements.append(pts)
    return placements


def can_pack(W, H, shapes, counts):
    max_idx = max(shapes.keys()) if shapes else -1
    cnt = list(counts) + [0] * (max_idx + 1 - len(counts))

    placements_by_type = {}
    for t, shape in shapes.items():
        if not shape:
            placements_by_type[t] = []
            continue
        orients = orientations(shape)
        plats = []
        seen = set()
        for o in orients:
            key = tuple(sorted(o))
            if key in seen:
                continue
            seen.add(key)
            p = generate_placements(o, W, H)
            plats.extend(p)
        placements_by_type[t] = plats

    total_area = 0
    for t, c in enumerate(cnt):
        if c <= 0:
            continue
        if t not in shapes:
            return False
        total_area += len(shapes[t]) * c
    if total_area > W * H:
        return False

    board = [[False] * W for _ in range(H)]

    remaining = {t: cnt[t] for t in range(len(cnt)) if t in shapes and cnt[t] > 0}

    cover_index = defaultdict(lambda: defaultdict(list))
    for t, plats in placements_by_type.items():
        for p in plats:
            for x, y in p:
                cover_index[(x, y)][t].append(p)

    sys.setrecursionlimit(10000)

    def find_first_empty():
        for y in range(H):
            for x in range(W):
                if not board[y][x]:
                    return x, y
        return None

    def place(p):
        for x, y in p:
            board[y][x] = True

    def unplace(p):
        for x, y in p:
            board[y][x] = False

    def fits(p):
        for x, y in p:
            if board[y][x]:
                return False
        return True

    def search(remaining_count):
        if not any(remaining_count.values()):
            return True
        empt = find_first_empty()
        if empt is None:
            return False
        x0, y0 = empt
        types = list(remaining_count.keys())
        types.sort(key=lambda t: len(cover_index[(x0, y0)].get(t, [])))
        for t in types:
            if remaining_count.get(t, 0) <= 0:
                continue
            plats = cover_index[(x0, y0)].get(t, [])
            for p in plats:
                if fits(p):
                    place(p)
                    remaining_count[t] -= 1
                    if search(remaining_count):
                        return True
                    remaining_count[t] += 1
                    unplace(p)
        return False

    return search(remaining)


with open('input.txt') as f:
    input_text = f.read()
shapes, regions = parse_input(input_text)
for W, H, counts in regions:
    if can_pack(W, H, shapes, counts):
        print("YES")
    else:
        print("NO")