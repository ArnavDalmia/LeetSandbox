
import math

def kokoEatingBananasFunctionality(piles, h):
    if sum(piles) <= h:
        return 1
    left = 1
    right = max(piles)
    
    res = right
    while left <= right:
        k = (left + right) // 2
        
        total = 0
        for pile in piles:
            total += math.ceil(float(pile) / k)
        
        if total <= h:
            res = k
            right = k - 1
        else:
            left = k + 1
    return res

def main(piles, h):
    result = kokoEatingBananasFunctionality(piles, h)
    
    output = f"""Banana piles: {piles}
Hours available: {h}
Minimum eating speed (bananas per hour): {result}"""
    
    # Verify the solution
    total_hours = 0
    for pile in piles:
        hours_for_pile = math.ceil(pile / result)
        total_hours += hours_for_pile
        output += f"\n  Pile of {pile} bananas takes {hours_for_pile} hours at speed {result}"
    
    output += f"\nTotal hours needed: {total_hours}"
    output += f"\nWithin time limit: {'✓' if total_hours <= h else '✗'}"
    
    # Show binary search process
    output += "\n\nBinary search process:"
    left, right = 1, max(piles)
    step = 1
    
    while left <= right:
        k = (left + right) // 2
        total = sum(math.ceil(pile / k) for pile in piles)
        
        output += f"\n  Step {step}: k={k}, total_hours={total}"
        
        if total <= h:
            output += f"\n    {total} <= {h}: Can finish in time, try slower speed"
            right = k - 1
        else:
            output += f"\n    {total} > {h}: Too slow, need faster speed"
            left = k + 1
        step += 1
    
    return output

# EXAMPLE
# main([3, 6, 7, 11], 8)
# main([30, 11, 23, 4, 20], 5)
