
def containsDuplicateFunctionality(nums):
    myDict = {}
    for i in range(len(nums)):
        if nums[i] in myDict:
            return True
        else:
            myDict[nums[i]] = i
    return False

def main(nums):
    result = containsDuplicateFunctionality(nums)
    
    output = f"Array: {nums}\n"
    if result:
        output += "Result: Contains duplicate"
    else:
        output += "Result: No duplicates found"
    
    return output

# EXAMPLE
# main([1, 2, 3, 1])
# main([1, 2, 3, 4])
