
def longestConsecutiveFunctionality(nums):
    if not nums:
        return 0

    result = set(nums)
    streak = 0

    for i in result:
        if (i-1) not in result:
            length = 1
            while (i+length) in result:
                length += 1
            streak = max(length, streak)

    return streak

def main(nums):
    result = longestConsecutiveFunctionality(nums)
    
    output = f"""Array: {nums}
Longest consecutive sequence length: {result}"""
    
    # Show the consecutive sequences found
    if nums:
        num_set = set(nums)
        sequences = []
        
        for num in num_set:
            if (num - 1) not in num_set:  # Start of a sequence
                current_sequence = [num]
                current_num = num
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_sequence.append(current_num)
                sequences.append(current_sequence)
        
        output += "\nConsecutive sequences found:"
        for seq in sorted(sequences, key=len, reverse=True):
            output += f"\n  {seq} (length: {len(seq)})"
    
    return output

# EXAMPLE
# main([100, 4, 200, 1, 3, 2])
# main([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
