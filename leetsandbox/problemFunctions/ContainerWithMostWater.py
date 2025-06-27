
def shorter(one, two, nums):
    if nums[one] < nums[two]:
        return nums[one]
    else:
        return nums[two]

def containerWithMostWaterFunctionality(nums):
    maxArea = 0
    left, right = 0, len(nums) - 1

    # now we have indexes
    while left < right:
        tempArea = shorter(left, right, nums) * (right - left)
        if tempArea > maxArea:
            maxArea = tempArea

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return maxArea

def main(height):
    result = containerWithMostWaterFunctionality(height)
    
    # Show how the algorithm works
    explanation = f"""Heights: {height}
Maximum water area: {result}

Two-pointer approach explanation:"""
    
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        explanation += f"\n  Left: {left} (height={height[left]}), Right: {right} (height={height[right]}), Area: {current_area}"
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        
        if left >= right:
            break
    
    return explanation

# EXAMPLE
# main([1, 8, 6, 2, 5, 4, 8, 3, 7])
# main([1, 1])
