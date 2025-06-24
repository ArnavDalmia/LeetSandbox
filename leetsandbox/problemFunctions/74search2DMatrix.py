
def search(nums, target):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        m = ((r - l) // 2) + l
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return True
    return False

def search2DMatrixFunctionality(matrix, target):
    rows = len(matrix)
    if rows >= 1:
        sizeOfRow = len(matrix[0])
    else:
        return False
    
    # Check if target is within matrix bounds
    if not (target <= matrix[rows-1][sizeOfRow-1] and target >= matrix[0][0]):
        return False
    
    # Binary search to find the correct row
    l = 0
    r = rows - 1
    while l <= r:
        m = ((r - l) // 2) + l
        if (matrix[m][0]) > target:
            r = m - 1
        elif (matrix[m][sizeOfRow-1]) < target:
            l = m + 1
        else:
            return search(matrix[m], target)
    return False

def main(matrix, target):
    result = search2DMatrixFunctionality(matrix, target)
    print(f"2D Matrix:")
    for row in matrix:
        print(f"  {row}")
    print(f"Target: {target}")
    print(f"Found: {result}")
    
    # Show the search process
    print("\nSearch process:")
    rows = len(matrix)
    if rows == 0:
        print("  Empty matrix")
        return
    
    cols = len(matrix[0])
    print(f"  Matrix bounds: {matrix[0][0]} to {matrix[rows-1][cols-1]}")
    
    if not (matrix[0][0] <= target <= matrix[rows-1][cols-1]):
        print("  Target outside matrix bounds")
        return
    
    # Binary search for row
    l, r = 0, rows - 1
    step = 1
    while l <= r:
        m = (l + r) // 2
        print(f"  Step {step}: Checking row {m}: [{matrix[m][0]} ... {matrix[m][cols-1]}]")
        
        if matrix[m][0] > target:
            print(f"    Target {target} < {matrix[m][0]}, search upper rows")
            r = m - 1
        elif matrix[m][cols-1] < target:
            print(f"    Target {target} > {matrix[m][cols-1]}, search lower rows")
            l = m + 1
        else:
            print(f"    Target {target} might be in row {m}, searching row...")
            # Binary search within the row
            row_l, row_r = 0, cols - 1
            row_step = 1
            while row_l <= row_r:
                row_m = (row_l + row_r) // 2
                print(f"      Row step {row_step}: Checking position {row_m}, value {matrix[m][row_m]}")
                if matrix[m][row_m] == target:
                    print(f"      Found target at row {m}, col {row_m}!")
                    return
                elif matrix[m][row_m] > target:
                    row_r = row_m - 1
                else:
                    row_l = row_m + 1
                row_step += 1
            print(f"      Target not found in row {m}")
            return
        step += 1

# EXAMPLE
# main([[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], 5)
# main([[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], 13)
