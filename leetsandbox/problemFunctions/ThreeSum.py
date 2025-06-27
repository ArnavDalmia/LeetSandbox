
def threeSumFunctionality(nums):
    res = []
    nums.sort()

    for i in nums:
        if i > 0:
            hasOnlyPositive = True
        else:
            hasOnlyPositive = False
            break
    for i in nums:
        if i < 0:
            hasOnlyNegative = True
        else:
            hasOnlyNegative = False
            break
    if hasOnlyPositive or hasOnlyNegative:
        return []

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        
        l, r = i+1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return res

def main(nums):
    result = threeSumFunctionality(nums)
    
    output = f"""Array: {nums}
Three sum triplets that equal 0:"""
    
    if result:
        for triplet in result:
            output += f"\n  {triplet}"
        output += f"\nTotal triplets found: {len(result)}"
    else:
        output += "\n  No triplets found that sum to 0"
    
    return output

# EXAMPLE
# main([-1, 0, 1, 2, -1, -4])
# main([0, 1, 1])
