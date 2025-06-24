
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
    print(f"Array: {nums}")
    if result:
        print("Result: Contains duplicate")
    else:
        print("Result: No duplicates found")

# EXAMPLE
# main([1, 2, 3, 1])
# main([1, 2, 3, 4])
