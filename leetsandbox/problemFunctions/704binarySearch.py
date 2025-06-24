
def binarySearchFunctionality(nums, target):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        m = ((r - l) // 2) + l
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1

def main(nums, target):
    result = binarySearchFunctionality(nums, target)
    print(f"Array: {nums}")
    print(f"Target: {target}")
    if result != -1:
        print(f"Result: Target found at index {result}")
    else:
        print("Result: Target not found")

# EXAMPLE
# main([-1, 0, 3, 5, 9, 12], 9)
# main([-1, 0, 3, 5, 9, 12], 2)
