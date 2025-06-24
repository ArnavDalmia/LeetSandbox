
def findMinInRotatedSortedArrayFunctionality(nums):
    l, r = 0, len(nums) - 1
    
    result = nums[0]

    while l <= r:
        if nums[l] < nums[r]:
            result = min(result, nums[l])
            break
        m = ((r + l) // 2)
        result = min(result, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return result

def main(nums):
    result = findMinInRotatedSortedArrayFunctionality(nums)
    
    output = f"""Rotated sorted array: {nums}
Minimum element: {result}

Binary search process:"""
    
    # Show the binary search process
    l, r = 0, len(nums) - 1
    result_track = nums[0]
    step = 1
    
    while l <= r:
        output += f"\n  Step {step}: l={l}, r={r}, current_min={result_track}"
        
        if nums[l] < nums[r]:
            result_track = min(result_track, nums[l])
            output += f"\n  Array portion is sorted, min is {nums[l]}"
            break
            
        m = (l + r) // 2
        result_track = min(result_track, nums[m])
        output += f"\n  Middle index {m}, value {nums[m]}, updated min: {result_track}"
        
        if nums[m] >= nums[l]:
            output += f"\n  Left half is sorted, search right half"
            l = m + 1
        else:
            output += f"\n  Right half is sorted, search left half"
            r = m - 1
        step += 1
    
    return output

# EXAMPLE
# main([3, 4, 5, 1, 2])
# main([4, 5, 6, 7, 0, 1, 2])
# main([11, 13, 15, 17])
