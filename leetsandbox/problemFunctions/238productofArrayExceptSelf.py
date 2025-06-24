
def productExceptSelfFunctionality(nums):
    total = 1
    for i in nums:
        if i != 0:
            total = total * i
    # have total
    # now we have total
    countVar = nums.count(0)
    if countVar >= 2:
        return [0] * len(nums)
    elif countVar == 1:
        indexOfZero = nums.index(0)
        temp = [0] * len(nums)
        temp[indexOfZero] = total
        return temp
    else:
        temp = []
        for i in nums:
            temp.append(total // i)
        return temp

def main(nums):
    result = productExceptSelfFunctionality(nums)
    
    output = f"""Input array: {nums}
Product of array except self: {result}

Explanation:"""
    
    # Show explanation
    for i in range(len(nums)):
        others = [nums[j] for j in range(len(nums)) if j != i]
        output += f"\n  Index {i}: product of {others} = {result[i]}"
    
    return output

# EXAMPLE
# main([1, 2, 3, 4])
# main([-1, 1, 0, -3, 3])
