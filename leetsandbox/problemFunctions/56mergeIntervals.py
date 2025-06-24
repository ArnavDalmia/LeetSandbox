
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
    print(f"Input intervals: {intervals}")
    print(f"Merged intervals: {result}")
    
    # Show the merge process step by step
    if intervals:
        print("Merge process:")
        sorted_intervals = sorted(intervals)
        print(f"  After sorting: {sorted_intervals}")
        
        merged = [sorted_intervals[0]]
        print(f"  Start with: {merged}")
        
        for i, (start, end) in enumerate(sorted_intervals[1:], 1):
            lastEnd = merged[-1][1]
            if start <= lastEnd:
                old_interval = merged[-1][:]
                merged[-1][1] = max(lastEnd, end)
                print(f"  Step {i}: Merge {old_interval} and [{start}, {end}] -> {merged[-1]}")
            else:
                merged.append([start, end])
                print(f"  Step {i}: Add [{start}, {end}] -> Current: {merged}")

# EXAMPLE
# main([[1, 3], [2, 6], [8, 10], [15, 18]])
# main([[1, 4], [4, 5]])
