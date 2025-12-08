from bisect import bisect_right
from typing import List, Tuple

def parse_input(lines: List[str]) -> Tuple[List[Tuple[int,int]], List[int]]:
    ranges = []
    ids = []
    it = iter(lines)
    for line in it:
        s = line.strip()
        if s == "":
            break
        if "-" in s:
            a,b = s.split("-",1)
            ranges.append((int(a), int(b)))
    for line in it:
        s = line.strip()
        if s:
            ids.append(int(s))
    return ranges, ids


def merge_ranges(ranges: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    if not ranges:
        return []
    ranges_sorted = sorted(ranges, key=lambda x: (x[0], x[1]))
    merged = []
    cur_start, cur_end = ranges_sorted[0]
    for a,b in ranges_sorted[1:]:
        if a <= cur_end + 1:
            cur_end = max(cur_end, b)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = a,b
    merged.append((cur_start, cur_end))
    return merged


def count_fresh(merged: List[Tuple[int,int]], ids: List[int]) -> int:
    if not merged or not ids:
        return 0
    starts = [s for s,_ in merged]
    ends = [e for _,e in merged]
    fresh = 0
    for x in ids:
        i = bisect_right(starts, x) - 1
        if i >= 0 and ends[i] >= x:
            fresh += 1
    return fresh

def total_fresh_ids(merged: List[Tuple[int, int]]) -> int:
    return sum((e - s + 1) for s, e in merged)


with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        ranges, ids = parse_input(lines)
        merged = merge_ranges(ranges)
        p1 = count_fresh(merged, ids)
        p2 = total_fresh_ids(merged)
        print(p1)
        print(p2)