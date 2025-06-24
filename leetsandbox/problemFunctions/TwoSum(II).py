def twoSumIIFunctionality(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        prod = numbers[left] + numbers[right]
        if prod == target:
            return [left + 1, right + 1]
        elif prod > target:
            right -= 1
        else:
            left += 1
    return []

def main(numbers, target):
    temp = twoSumIIFunctionality(numbers, target)
    print("Indexes of two numbers are: ")
    if temp != []:
        print(temp)
    else:
        print("ERROR: Pair does not exist. Try with another target or sorted array.")

# EXAMPLE
#main([2,7,11,15], 9)