
def searchInRotatedSortedArrayFunctionality(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = ((r + l) // 2)
        if nums[m] == target:
            return m
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1

def main(nums, target):
    result = searchInRotatedSortedArrayFunctionality(nums, target)
    print(f"Rotated sorted array: {nums}")
    print(f"Target: {target}")
    if result != -1:
        print(f"Result: Target found at index {result}")
    else:
        print("Result: Target not found")
    
    # Show the binary search process
    print("Binary search process:")
    l, r = 0, len(nums) - 1
    step = 1
    
    while l <= r:
        m = (l + r) // 2
        print(f"  Step {step}: l={l}, r={r}, m={m}, nums[m]={nums[m]}")
        
        if nums[m] == target:
            print(f"  Found target at index {m}!")
            break
        elif nums[l] <= nums[m]:  # Left half is sorted
            if nums[l] <= target < nums[m]:
                print(f"  Target in left half, search left")
                r = m - 1
            else:
                print(f"  Target in right half, search right")
                l = m + 1
        else:  # Right half is sorted
            if nums[m] < target <= nums[r]:
                print(f"  Target in right half, search right")
                l = m + 1
            else:
                print(f"  Target in left half, search left")
                r = m - 1
        step += 1

# EXAMPLE
# main([4, 5, 6, 7, 0, 1, 2], 0)
# main([4, 5, 6, 7, 0, 1, 2], 3)
