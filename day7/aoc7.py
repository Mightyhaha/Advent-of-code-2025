def solve1(input_text):
    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    start_row, start_col = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
                break
        if start_row is not None:
            break
    
    if start_row is None:
        return 0
    
    beams = [(start_row, start_col, 'D')]
    split_count = 0
    visited = set()
    
    while beams:
        row, col, direction = beams.pop(0)
        
        state = (row, col, direction)
        if state in visited:
            continue
        visited.add(state)
        
        if direction == 'D':
            row += 1
        elif direction == 'L':
            col -= 1
        elif direction == 'R':
            col += 1
        
        if row < 0 or row >= rows or col < 0 or col >= cols:
            continue
        
        cell = grid[row][col]
        
        if cell == '^':
            split_count += 1
            beams.append((row, col - 1, 'D'))
            beams.append((row, col + 1, 'D'))
        else:
            beams.append((row, col, direction))
    
    return split_count


def solve2(input_text):
    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    start_row, start_col = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
                break
        if start_row is not None:
            break
    
    if start_row is None:
        return 0
    
    # This is the worst way ive tried to optimized this
    timeline_count = {}
    timeline_count[(start_row, start_col, 'D')] = 1
    
    queue = [(start_row, start_col, 'D')]
    seen = set()
    
    while queue:
        state = queue.pop(0)
        if state in seen:
            continue
        seen.add(state)
        
        row, col, direction = state
        count = timeline_count[state]
        
        if direction == 'D':
            row += 1
        elif direction == 'L':
            col -= 1
        elif direction == 'R':
            col += 1
        
        if row < 0 or row >= rows or col < 0 or col >= cols:
            continue
        
        cell = grid[row][col]
        
        if cell == '^':
            left_state = (row, col - 1, 'D')
            right_state = (row, col + 1, 'D')
            
            timeline_count[left_state] = timeline_count.get(left_state, 0) + count
            timeline_count[right_state] = timeline_count.get(right_state, 0) + count
            
            if left_state not in seen:
                queue.append(left_state)
            if right_state not in seen:
                queue.append(right_state)
        else:
            next_state = (row, col, direction)
            timeline_count[next_state] = timeline_count.get(next_state, 0) + count
            
            if next_state not in seen:
                queue.append(next_state)
    
    exit_timelines = 0
    for (r, c, d), count in timeline_count.items():
        next_r, next_c = r, c
        if d == 'D':
            next_r += 1
        elif d == 'L':
            next_c -= 1
        elif d == 'R':
            next_c += 1
        
        if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
            exit_timelines += count
    
    return exit_timelines


with open('input.txt', 'r') as f:
    input_text = f.read()

result1 = solve1(input_text)
print(result1)
result2 = solve2(input_text)
print(result2)
