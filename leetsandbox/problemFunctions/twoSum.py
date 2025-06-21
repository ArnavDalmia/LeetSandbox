def twoSumFunctionality(nums, target):
    myDict = {}
    for i in range(len(nums)): #nums[i] is the value i am checking
        num = target - nums[i]
        if num in myDict:
            return [myDict[num], i]
        else:
            myDict[nums[i]] = i
    return []

def main(nums, target):
    temp = twoSumFunctionality(nums, target)
    print("Indexes of two numbers are: ")
    if temp != []:
        return temp
    else:
        return ("ERROR: Pair does not exist. Try with another target or list of numbers.")

# import main, call function with set parameters from user input

#EXAMPLE
#print(main([1,2,3,4],8)))