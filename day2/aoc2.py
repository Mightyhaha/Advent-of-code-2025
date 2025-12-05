def is_invalid_id(num):
    s = str(num)
    length = len(s)
    
    for seq_len in range(1, length // 2 + 1):
        if length % seq_len == 0:
            sequence = s[:seq_len]
            if sequence * (length // seq_len) == s:
                return True
    return False


def find_invalid_ids_in_range(start, end):
    invalid_ids = []
    seq_len = 1
    while True:
        min_invalid = int(str(10 ** (seq_len - 1)) * 2)
        
        if min_invalid > end:
            break
        
        for base in range(10 ** (seq_len - 1), 10 ** seq_len):
            for repetitions in range(2, 10):
                invalid_id = int(str(base) * repetitions)
                if invalid_id > end:
                    break
                if invalid_id >= start:
                    invalid_ids.append(invalid_id)
        
        seq_len += 1
    
    return sorted(set(invalid_ids))


def solve(ranges_input):
    ranges = []
    for range_str in ranges_input.split(','):
        range_str = range_str.strip()
        if range_str:
            start, end = map(int, range_str.split('-'))
            ranges.append((start, end))
    
    total_sum = 0
    for start, end in ranges:
        invalid_ids = find_invalid_ids_in_range(start, end)
        total_sum += sum(invalid_ids)
    return total_sum


example_input = "990244-1009337,5518069-5608946,34273134-34397466,3636295061-3636388848,8613701-8663602,573252-688417,472288-533253,960590-988421,7373678538-7373794411,178-266,63577667-63679502,70-132,487-1146,666631751-666711926,5896-10827,30288-52204,21847924-21889141,69684057-69706531,97142181-97271487,538561-555085,286637-467444,93452333-93519874,69247-119122,8955190262-8955353747,883317-948391,8282803943-8282844514,214125-236989,2518-4693,586540593-586645823,137643-211684,33-47,16210-28409,748488-837584,1381-2281,1-19"

result = solve(example_input)
print(result)