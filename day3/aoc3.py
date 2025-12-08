def solve_batteries(input_str):
    lines = input_str.strip().split('\n')
    total_output = 0
    
    for line in lines:
        if not line:
            continue

        digits = [int(d) for d in line]
        max_joltage = 0
        
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                joltage = digits[i] * 10 + digits[j]
                max_joltage = max(max_joltage, joltage)
        
        total_output += max_joltage
    return total_output


def solve_batteries2(input_str):
    lines = input_str.strip().split('\n')
    total_output = 0
    
    for line in lines:
        if not line:
            continue
        
        digits = [int(d) for d in line]
        n = len(digits)

        if n < 12:
            joltage_str = ''.join(str(d) for d in digits)
            joltage = int(joltage_str) if joltage_str else 0
            total_output += joltage
            continue
        
        num_to_remove = n - 12
        kept = []
        
        for i in range(n):
            while kept and kept[-1] < digits[i] and num_to_remove > 0:
                kept.pop()
                num_to_remove -= 1
            
            kept.append(digits[i])
        
        while num_to_remove > 0:
            kept.pop()
            num_to_remove -= 1
        
        joltage_str = ''.join(str(d) for d in kept[:12])
        joltage = int(joltage_str)
        total_output += joltage
    return total_output

with open('input.txt', 'r') as f:
    puzzle_input = f.read()
    print(solve_batteries(puzzle_input))
    print(solve_batteries2(puzzle_input))
