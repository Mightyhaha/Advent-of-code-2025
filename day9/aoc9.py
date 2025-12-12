def solve1(input_text: str) -> int:
    lines = input_text.strip().split('\n')
    coordinates = []
    
    for line in lines:
        if line.strip():
            x, y = map(int, line.strip().split(','))
            coordinates.append((x, y))
    
    max_area = 0
    
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            
            max_area = max(max_area, area)
    
    return max_area

with open('input.txt', 'r') as f:
    input_data = f.read()
    print(solve1(input_data))
