
def mergeIntervalsFunctionality(intervals):
    if not intervals:
        return []
        
    intervals.sort()
    answer = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = answer[-1][1]
        if start <= lastEnd:
            answer[-1][1] = max(lastEnd, end)
        else:
            answer.append([start, end])
    return answer

def main(intervals):
    result = mergeIntervalsFunctionality(intervals)
    
    output = f"""Input intervals: {intervals}
Merged intervals: {result}"""
    
    # Show the merge process step by step
    if intervals:
        output += "\nMerge process:"
        sorted_intervals = sorted(intervals)
        output += f"\n  After sorting: {sorted_intervals}"
        
        merged = [sorted_intervals[0]]
        output += f"\n  Start with: {merged}"
        
        for i, (start, end) in enumerate(sorted_intervals[1:], 1):
            lastEnd = merged[-1][1]
            if start <= lastEnd:
                old_interval = merged[-1][:]
                merged[-1][1] = max(lastEnd, end)
                output += f"\n  Step {i}: Merge {old_interval} and [{start}, {end}] -> {merged[-1]}"
            else:
                merged.append([start, end])
                output += f"\n  Step {i}: Add [{start}, {end}] -> Current: {merged}"
    
    return output

# EXAMPLE
# main([[1, 3], [2, 6], [8, 10], [15, 18]])
# main([[1, 4], [4, 5]])
