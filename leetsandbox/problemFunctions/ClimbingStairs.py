def climbingStairsFunctionality(n):
    # Using dynamic programming approach
    # Each step can be reached by either taking 1 step from (n-1) or 2 steps from (n-2)
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one

def main(n):
    result = climbingStairsFunctionality(n)
    
    output = f"""Number of stairs: {n}
Number of distinct ways to climb: {result}"""
    
    return output

# EXAMPLE
# main(5)
# main(3)
