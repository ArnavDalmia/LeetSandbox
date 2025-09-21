import collections
from collections import deque

def numberOfIslandsFunctionality(grid):
    if not grid:
        return 0
    
    islands = 0
    rows, cols = len(grid), len(grid[0])
    visit = set()

    def bfs(r, c):
        q = deque()
        visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and c in range(cols) and 
                    grid[r][c] == "1" and (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))
   
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands

def main(grid):
    result = numberOfIslandsFunctionality(grid)
    
    output = f"""Grid:
{chr(10).join([str(row) for row in grid])}
Number of islands: {result}"""
    
    return output

# EXAMPLE
# main([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
# main([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])     
        