
def subarraySumFunctionality(nums, k):
    count = 0  # cumulative sum
    my_dict = {}
    my_dict[0] = 1
    result = 0
    
    for index in range(len(nums)):
        count += nums[index]
        target = count - k
        if target in my_dict:
            result += my_dict[target]
        
        if count in my_dict:
            my_dict[count] += 1
        else:
            my_dict[count] = 1
    
    return result

def findSubarrays(nums, k):
    """Find all subarrays that sum to k"""
    subarrays = []
    
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == k:
                subarrays.append((i, j, nums[i:j+1]))
    
    return subarrays

def main(nums, k):
    result = subarraySumFunctionality(nums, k)
    subarrays = findSubarrays(nums, k)
    
    output = f"""Array: {nums}
Target sum: {k}
Number of subarrays with sum {k}: {result}

Subarrays found:"""
    
    if subarrays:
        for i, (start_idx, end_idx, subarray) in enumerate(subarrays):
            output += f"\n  {i + 1}. {subarray} (indices {start_idx}-{end_idx})"
    else:
        output += "\n  No subarrays found with the target sum"
    
    return output

# EXAMPLE
# main([1, -1, 1, 1, 1, 1], 3)
# main([1, 1, 1], 2)



