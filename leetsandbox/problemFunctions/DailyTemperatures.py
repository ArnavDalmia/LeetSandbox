
def dailyTemperaturesFunctionality(temperatures):
    stack = []
    res = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            val, ind = stack.pop()
            res[ind] = i - ind
        stack.append((t, i))
    return res

def main(temperatures):
    result = dailyTemperaturesFunctionality(temperatures)
    
    output = f"""Daily temperatures: {temperatures}
Days to wait for warmer temperature: {result}

Stack-based process:"""
    
    # Show the process step by step
    stack = []
    res = [0] * len(temperatures)
    
    for i, temp in enumerate(temperatures):
        output += f"\n  Day {i}: Temperature {temp}"
        
        # Process stack while current temp is warmer
        while stack and temp > stack[-1][0]:
            prev_temp, prev_day = stack.pop()
            days_to_wait = i - prev_day
            res[prev_day] = days_to_wait
            output += f"\n    Found warmer day for day {prev_day} (temp {prev_temp}): {days_to_wait} days"
        
        # Add current day to stack
        stack.append((temp, i))
        output += f"\n    Stack: {[(t, d) for t, d in stack]}"
        output += f"\n    Result so far: {res}"
    
    output += f"\nFinal result: {res}"
    
    return output

# EXAMPLE
# main([73, 74, 75, 71, 69, 72, 76, 73])
# main([30, 40, 50, 60])
